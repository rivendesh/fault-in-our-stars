from __future__ import annotations

from pathlib import Path
from typing import Optional
import argparse
import gc
import pickle
import sys
import types

import numpy as np
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
ARTIFACT_DIR = BASE_DIR / "artifacts"
ARTIFACT_DIR.mkdir(exist_ok=True)
SEQ_LEN = 256


def ensure_numpy_pickle_compat() -> None:
    aliases = {
        "numpy._core": "numpy.core",
        "numpy._core.numeric": "numpy.core.numeric",
        "numpy._core.multiarray": "numpy.core.multiarray",
        "numpy._core.umath": "numpy.core.umath",
        "numpy._core._multiarray_umath": "numpy.core._multiarray_umath",
    }
    for old_name, new_name in aliases.items():
        if old_name not in sys.modules:
            sys.modules[old_name] = __import__(new_name, fromlist=["*"])


class _LegacyStringArrayCompat:
    """Array-like shim for legacy pandas StringArray pickle state."""

    def __init__(self) -> None:
        self.data = None

    def __setstate__(self, state) -> None:
        if isinstance(state, tuple) and len(state) == 2:
            self.data = np.asarray(state[1], dtype=object)
        else:
            self.data = np.asarray(state, dtype=object)

    def __len__(self) -> int:
        return len(self.data)

    def __iter__(self):
        return iter(self.data)

    def __array__(self, dtype=None):
        return np.asarray(self.data, dtype=dtype)

    @property
    def dtype(self):
        return object


class _CompatUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        if (module, name) == ("pandas._libs.arrays", "__pyx_unpickle_NDArrayBacked"):
            def custom(cls, checksum, state):
                return _LegacyStringArrayCompat()

            return custom
        return super().find_class(module, name)


def read_pickle_compat(path: Path) -> pd.DataFrame:
    ensure_numpy_pickle_compat()
    try:
        df = pd.read_pickle(path)
    except NotImplementedError as exc:
        if "NDArrayBacked" not in str(exc) and "StringDtype" not in str(exc) and "array([" not in str(exc):
            raise
        with open(path, "rb") as fh:
            df = _CompatUnpickler(fh).load()
    if not isinstance(df, pd.DataFrame):
        raise TypeError(f"Expected DataFrame in {path}, got {type(df)}")
    return df


def normalize_dataframe(df: pd.DataFrame) -> pd.DataFrame:
    if "KIC" not in df.columns and df.index.name == "KIC":
        df = df.reset_index()
    if "# ID" not in df.columns and df.index.name == "# ID":
        df = df.reset_index()
    return df


def infer_id_column(df: pd.DataFrame) -> str:
    for col in ["KIC", "kepid", "# ID", "id"]:
        if col in df.columns:
            return col
    raise KeyError(f"No ID column found in columns: {list(df.columns)}")


def infer_flux_column(df: pd.DataFrame) -> str:
    for col in ["detflux", "flux", "PDCSAP_FLUX"]:
        if col in df.columns:
            return col
    raise KeyError(f"No flux column found in columns: {list(df.columns)}")


def infer_label_column(df: pd.DataFrame) -> str:
    for col in ["Class", "class", "label", "Label"]:
        if col in df.columns:
            return col
    raise KeyError(f"No label column found in columns: {list(df.columns)}")


def to_float_array(values) -> np.ndarray:
    arr = np.asarray(values, dtype=np.float32).reshape(-1)
    return arr[np.isfinite(arr)]


def resample_sequence(values: np.ndarray, fixed_len: int = SEQ_LEN) -> np.ndarray:
    values = to_float_array(values)
    if len(values) == 0:
        return np.zeros(fixed_len, dtype=np.float32)
    if len(values) == 1:
        return np.repeat(values, fixed_len).astype(np.float32)

    x_old = np.linspace(0.0, 1.0, len(values), dtype=np.float32)
    x_new = np.linspace(0.0, 1.0, fixed_len, dtype=np.float32)
    seq = np.interp(x_new, x_old, values).astype(np.float32)

    mean = float(seq.mean())
    std = float(seq.std())
    if std < 1e-6:
        return (seq - mean).astype(np.float32)
    return ((seq - mean) / std).astype(np.float32)


def build_sequence(group: pd.DataFrame, flux_col: str) -> np.ndarray:
    if "quarter" in group.columns:
        group = group.sort_values("quarter")

    parts = []
    for _, row in group.iterrows():
        arr = to_float_array(row[flux_col])
        if len(arr) > 0:
            parts.append(arr)

    if not parts:
        return np.zeros(SEQ_LEN, dtype=np.float32)

    return resample_sequence(np.concatenate(parts), fixed_len=SEQ_LEN)


def remap_label(label: str) -> Optional[str]:
    normalized = str(label).strip().upper()
    mapping = {
        "CONFIRMED": "confirmed",
        "FALSE POSITIVE": "false positives",
        "CANDIDATE": None,
        "NOISE": "false positives",
        "EA": "eclipsing binary",
        "EB": "eclipsing binary",
        "BINARY": "eclipsing binary",
        "GDOR": "variable stars",
        "RRAB": "variable stars",
        "OTHPER": "variable stars",
        "DSCUT": "variable stars",
    }
    return mapping.get(normalized, None)


def read_koi_catalog_labels(csv_path: Path) -> pd.Series:
    catalog = pd.read_csv(csv_path, comment="#")
    catalog["kepid"] = pd.to_numeric(catalog["kepid"], errors="coerce").astype("Int64")
    catalog["koi_disposition"] = catalog["koi_disposition"].astype(str).str.strip().str.upper()
    catalog = catalog.dropna(subset=["kepid", "koi_disposition"])

    priority = ["CONFIRMED", "FALSE POSITIVE", "CANDIDATE"]

    def collapse(group: pd.Series) -> Optional[str]:
        values = set(group.tolist())
        for label in priority:
            if label in values:
                return label
        return None

    label_map = catalog.groupby("kepid")["koi_disposition"].apply(collapse).dropna()
    label_map.index = label_map.index.astype(int)
    return label_map


def dataset_artifact_paths(dataset_name: str) -> tuple[Path, Path]:
    return ARTIFACT_DIR / f"{dataset_name}_X.npy", ARTIFACT_DIR / f"{dataset_name}_meta.csv"


def process_and_save_dataset(pickle_path: Path, dataset_name: str, koi_label_map: Optional[pd.Series] = None) -> tuple[Path, Path]:
    print(f"Loading {pickle_path} ...", flush=True)
    df = normalize_dataframe(read_pickle_compat(pickle_path))
    id_col = infer_id_column(df)
    flux_col = infer_flux_column(df)
    label_col = infer_label_column(df) if dataset_name == "c00" else None

    keep_cols = [id_col, flux_col]
    if "quarter" in df.columns:
        keep_cols.append("quarter")
    if label_col is not None:
        keep_cols.append(label_col)
    df = df[keep_cols].copy()

    df[id_col] = pd.to_numeric(df[id_col], errors="coerce")
    df = df.dropna(subset=[id_col]).copy()
    df[id_col] = df[id_col].astype(int)

    sequences = []
    records = []

    grouped = df.groupby(id_col, sort=False)
    total_groups = grouped.ngroups
    print(f"Groups to process: {total_groups}", flush=True)

    for idx, (object_id, group) in enumerate(grouped, start=1):
        if dataset_name == "villanova":
            label = "binary"
        elif dataset_name == "koi":
            if koi_label_map is None or object_id not in koi_label_map.index:
                continue
            label = str(koi_label_map.loc[object_id]).strip().upper()
        elif dataset_name == "c00":
            label = str(group[label_col].iloc[0]).strip()
        else:
            raise ValueError(f"Unsupported dataset name: {dataset_name}")

        label = remap_label(label)

        if label is None or label == "" or label.lower() == "nan":
            continue

        sequences.append(build_sequence(group, flux_col))
        records.append({"dataset": dataset_name, "object_id": object_id, "label": label})

        if idx % 2000 == 0:
            print(f"Processed {idx}/{total_groups} groups", flush=True)

    if not sequences:
        raise RuntimeError(f"No sequences generated from {pickle_path}")

    X = np.stack(sequences).astype(np.float32)
    meta = pd.DataFrame(records)
    x_path, meta_path = dataset_artifact_paths(dataset_name)
    np.save(x_path, X)
    meta.to_csv(meta_path, index=False)

    print(f"Saved sequences: {x_path}", flush=True)
    print(f"Saved metadata: {meta_path}", flush=True)
    print(f"Final shape: {X.shape}", flush=True)
    print(meta["label"].value_counts(), flush=True)

    del df, grouped, sequences, records, X, meta
    gc.collect()
    return x_path, meta_path


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dataset", required=True, choices=["c00", "villanova", "koi"])
    args = parser.parse_args()

    dataset_to_path = {
        "c00": BASE_DIR / "C_00_LC_DATA.pkl",
        "villanova": BASE_DIR / "villanova-kepler-binaries-lcs.pkl",
        "koi": BASE_DIR / "koi_cumulative_lcs.pkl",
    }

    koi_label_map = None
    if args.dataset == "koi":
        koi_label_map = read_koi_catalog_labels(BASE_DIR / "cumulative_koi.csv")

    process_and_save_dataset(dataset_to_path[args.dataset], args.dataset, koi_label_map=koi_label_map)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
