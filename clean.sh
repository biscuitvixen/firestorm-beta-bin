#!/usr/bin/env bash
echo "🧹 Cleaning up build artifacts..."
rm -v *.pkg.tar.zst *.tar.xz 2>/dev/null || true
rm -rf src/ pkg/
echo "✅ Cleanup complete."