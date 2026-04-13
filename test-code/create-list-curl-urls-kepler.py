import re
import requests
from pathlib import Path

# sample KICs (replace later with your dataset)
kics = [
    3863594,
    10417986,
    8912468,
    8758716,
    10855535,
    9472174,
    9612468,
]

def kepler_dir(kic):
    kic9 = f"{int(kic):09d}"
    return f"https://archive.stsci.edu/pub/kepler/lightcurves/{kic9[:4]}/{kic9}/"

lines = [
    "#!/usr/bin/env bash",
    "set -euo pipefail",
    ""
]

for kic in kics:
    url = kepler_dir(kic)

    print(f"Processing KIC {kic}...")

    r = requests.get(url, timeout=30)
    r.raise_for_status()

    # only long cadence light curves
    files = re.findall(r'href="([^"]+_llc\.fits)"', r.text)

    lines.append(f"# KIC {kic}")
    for f in files:
        full_url = url + f
        lines.append(f"curl -O {full_url}")  # <-- no quotes here
    lines.append("")

# write script
out = Path("download_kepler_lcs.sh")
out.write_text("\n".join(lines) + "\n")
out.chmod(0o755)

print(f"\nWrote {out}")