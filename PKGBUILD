# Maintainer: Alex Tharp <alex at toastercup dot io>
_appname="firestorm-beta"
pkgname="${_appname}-bin"
provides=("${_appname}")
conflicts=("${_appname}")
pkgver=7.1.13.78266
pkgrel=1
pkgdesc="Firestorm is a feature-packed third-party viewer for Second Life (beta version)"
url="https://www.firestormviewer.org/early-access-beta-downloads/"
license=("LGPL-2.1-or-later")
arch=("x86_64")
depends=(
  "apr-util"
  "dbus-glib"
  "glib2>=2.35"
  "glu"
  "lib32-libidn"
  "lib32-libsndfile"
  "lib32-util-linux"
  "lib32-zlib"
  "libbsd"
  "libgl"
  "libidn"
  "libjpeg-turbo"
  "libpng"
  "libxcrypt-compat"
  "libxml2"
  "libxss"
  "mesa"
  "nss"
  "openal"
  "sdl"
  "vlc"
  "zlib"
)
optdepends=(
  "alsa-lib: for ALSA support"
  "freealut: for OpenAL support"
  "gst-plugins-bad: for video support"
  "gst-plugins-good: for video support"
  "gst-plugins-ugly: for video support"
  "gstreamer: For video support - may need good, bad and ugly plugins"
  "lib32-alsa-lib: for ALSA support"
  "lib32-freealut: for OpenAL support"
  "lib32-libidn11: for legacy Vivox voice support - will soon be fully replaced by WebRTC"
  "libpulse: for PulseAudio support"
  "nvidia-utils: for NVIDIA support"
)
install="${_appname}.install"
_tardir="Phoenix-Firestorm-Betax64_AVX2-${pkgver//./-}"
source=(
  "https://downloads.firestormviewer.org/preview/linux/${_tardir}.tar.xz"
  "${_appname}.desktop"
)
sha256sums=(
  "3801fe5bb87fd4a600ea634b2f288ee0725af43e86b3d6d64ca1a54314196063"
  "3899e0f61cfe928543217754320246a4fb0659e39cc1d3c91296e8e80d3c6589"
)

package() {
  install -d "${pkgdir}/opt"
  cp -a "${srcdir}/${_tardir}" "${pkgdir}/opt/${_appname}"

  cd "${pkgdir}/opt/${_appname}"
  find "app_settings" "skins" -type f -execdir chmod 644 "{}" +

  install -D -m644 "${srcdir}/${_appname}.desktop" "${pkgdir}/usr/share/applications/${_appname}.desktop"
  install -D -m644 "firestorm_icon.png" "${pkgdir}/usr/share/pixmaps/${_appname}.png"

  install -d "${pkgdir}/usr/share/licenses/${pkgname}"
  install -m644 "LGPL-license.txt" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE"
  install -m644 "licenses.txt" "${pkgdir}/usr/share/licenses/${pkgname}/LICENSE.bundled"

  install -d "${pkgdir}/usr/bin"
  ln -s "/opt/${_appname}/firestorm" "${pkgdir}/usr/bin/${_appname}"
}
