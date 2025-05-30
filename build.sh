#!/usr/bin/env bash
set -euo pipefail

if [[ $# -lt 1 ]]; then
  echo "❌ Usage: ./build.sh <version>"
  exit 1
fi

VERSION="$1"

echo "🛠️  Running updater for version $VERSION..."
./update_firestorm.py "$VERSION"

echo "📦 Building package..."
makepkg -sifCc  # -s = install deps, -i = install after build, -fCc = clean before+after build
