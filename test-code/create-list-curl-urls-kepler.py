from pathlib import Path
import re
import requests

# sample KICs only
kics = [757076, 11446443, 8462852]

out = Path("download_kepler_lightcurves.sh")
lines = ["#!/usr/bin/env bash", "set -euo pipefail", ""]

for kic in kics:
    kic9 = f"{kic:09d}"
    prefix4 = kic9[:4]
    dir_url = f"https://archive.stsci.edu/pub/kepler/lightcurves/{prefix4}/{kic9}/"

    html = requests.get(dir_url, timeout=60)
    html.raise_for_status()

    # grab every .fits link in the directory listing
    hrefs = re.findall(r'href="([^"]+\.fits(?:\.gz)?)"', html.text, flags=re.IGNORECASE)

    lines.append(f"# KIC {kic}")
    for href in hrefs:
        # skip parent links and non-files if any sneak in
        if href.startswith("../"):
            continue
        file_url = dir_url + href
        lines.append(f'curl -O "{file_url}"')
    lines.append("")

out.write_text("\n".join(lines) + "\n")
out.chmod(0o755)

print(f"Wrote {out}")