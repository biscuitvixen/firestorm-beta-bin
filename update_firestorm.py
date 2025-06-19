#!/usr/bin/env python3

import argparse
import hashlib
import sys
from pathlib import Path
import requests

URL_TEMPLATE = "https://downloads.firestormviewer.org/preview/linux/Phoenix-Firestorm-Betax64_AVX2-{}.tar.xz"


def download_tarball(hyphen_version: str, dest: Path) -> Path:
    url = URL_TEMPLATE.format(hyphen_version)
    filename = dest / Path(url).name
    print(f"⬇️ Downloading {url} ...")
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
    except requests.HTTPError as e:
        if e.response.status_code == 404:
            print(f"❌ Error: Version not found at {url}")
            sys.exit(1)
        else:
            print(f"❌ HTTP error while downloading: {e}")
            sys.exit(1)
    except requests.RequestException as e:
        print(f"❌ Network error: {e}")
        sys.exit(1)

    with open(filename, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
                f.write(chunk)

    return filename


def calculate_sha256(filepath: Path) -> str:
    print("🔐 Calculating SHA256...")
    hash_sha256 = hashlib.sha256()
    with filepath.open("rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()


def update_pkgbuild(pkgbuild: Path, dotted_version: str, checksum: str):
    print("📝 Updating PKGBUILD...")
    updated_lines = []
    in_sha256sums = False
    md5_done = False

    for line in pkgbuild.read_text().splitlines():
        if line.startswith("pkgver="):
            updated_lines.append(f"pkgver={dotted_version}")
        elif line.startswith("sha256sums=("):
            in_sha256sums = True
            updated_lines.append(line)
        elif in_sha256sums and not md5_done:
            # Replace the first md5 line
            updated_lines.append(f'  "{checksum}"')
            md5_done = True
        elif in_sha256sums and md5_done and line.strip().endswith(")"):
            updated_lines.append(line)
            in_sha256sums = False
        else:
            updated_lines.append(line)

    pkgbuild.write_text("\n".join(updated_lines) + "\n")


def main():
    parser = argparse.ArgumentParser(description="Update Firestorm Beta AUR package.")
    parser.add_argument("version", help="New Firestorm version (e.g. 7.1.13.78191)")
    args = parser.parse_args()

    dotted_version = args.version
    hyphen_version = dotted_version.replace(".", "-")
    tarball_url = URL_TEMPLATE.format(hyphen_version)

    workdir = Path(__file__).resolve().parent
    pkgbuild_path = workdir / "PKGBUILD"

    tarball_path = download_tarball(hyphen_version, workdir)
    checksum = calculate_sha256(tarball_path)
    update_pkgbuild(pkgbuild_path, dotted_version, checksum)

    print(f"✅ Done. Updated to version {dotted_version}.")
    print("💡 Run: makepkg -si")


if __name__ == "__main__":
    main()