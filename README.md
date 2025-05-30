# 🔥 firestorm-beta-bin (custom AUR fork)

A personal fork of the [`firestorm-beta-bin`](https://aur.archlinux.org/packages/firestorm-beta-bin) AUR package, used to track and install the **Firestorm Beta Viewer** for Second Life on Arch Linux.

---

## 📦 What This Package Does

* Downloads and installs the **official precompiled Firestorm Beta binary** for Linux.
* Installs it to: `/opt/firestorm-beta`
* Adds a launch script and `.desktop` entry
* Includes version and SHA256 tracking for verification
* Can be installed and tracked via `yay` or `makepkg` directly

---

## 🔄 Why This Exists

The upstream `firestorm-beta-bin` package is frequently out-of-date. This fork:

* Is manually updated with the latest beta versions from [firestormviewer.org](https://www.firestormviewer.org/early-access-beta-downloads/)
* Provides correct SHA256 verification
* Can be installed and updated via `makepkg` or `yay` when set up properly

---

## 🚀 Installation

Clone and build manually:

```bash
git clone https://github.com/yourusername/firestorm-beta-bin ~/aur/firestorm-beta-bin
cd ~/aur/firestorm-beta-bin
makepkg -si
```

To keep control of updates, you may want to add the package to yay's ignore list:

```jsonc
// ~/.config/yay/config.json
{
  "IgnorePkg": ["firestorm-beta-bin"]
}
```

Then continue managing it manually.

---

## 🔁 Updating to the Latest Beta Version

*(Assumes you're in the `firestorm-beta-bin` directory)*

To update to the latest version, run the helper script followed by the new version number. For example:

```bash
./update_firestorm.py 7.1.13.78191
```

This updates all necessary version information, downloads the new tarball and recalculates the hashes.

Then build and install:

```bash
makepkg -si
```

To clean up old package files and caches:

```bash
makepkg -C
```

---

## 🧰 Helper Scripts

### `build.sh`

A convenience script that updates, builds, installs, and cleans in one step:

```bash
./build.sh 7.1.13.78191
```

This runs the Python updater, then executes:

```bash
makepkg -sifCc
```

Where:

* `-s` installs dependencies
* `-i` installs the package after building
* `-f` forces rebuild
* `-C` cleans before building
* `-c` cleans after building

### `clean.sh`

Cleans all leftover build and archive files:

```bash
./clean.sh
```

This removes `*.pkg.tar.zst`, `*.tar.xz`, and clears `src/` and `pkg/` folders.

---

## 🧠 Notes on yay Integration

If you haven't ignored this package via `IgnorePkg`, yay will:

* Detect if the **AUR version is newer** than your local version
* Automatically rebuild and install the newer AUR version

If your local version is newer, yay will skip it.

---

This package is maintained manually to ensure prompt availability of the latest Firestorm Beta releases on Arch Linux.
