from pathlib import Path
from astroquery.mast import Observations

kics = [757076, 11446443, 8462852]  # sample KICs only

lines = ["#!/usr/bin/env bash", "set -euo pipefail", ""]

for kic in kics:
    obs = Observations.query_criteria(
        obs_collection="Kepler",
        object_name=f"KIC {kic}",
    )

    products = Observations.get_product_list(obs)
    products = Observations.filter_products(
        products,
        extension="fits",
        productType="SCIENCE",
    )

    lines.append(f"# KIC {kic}")
    for row in products:
        url = f"https://mast.stsci.edu/api/v0.1/Download/file?uri={row['dataURI']}"
        lines.append(f'curl -L -O "{url}"')
    lines.append("")

Path("download_kepler_lightcurves.sh").write_text("\n".join(lines) + "\n")
print("Wrote download_kepler_lightcurves.sh")