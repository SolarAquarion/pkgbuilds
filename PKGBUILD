# Maintainer: Yurii Kolesnykov <root@yurikoles.com>
# Contributor: Solomon Choina <shlomochoina@gmail.com>

pkgname=kcm-grub2-git
_product="${pkgname%-git}"
pkgver=0.6.4.r86.g1912ede
pkgrel=2
pkgdesc="A KDE Control Module for configuring the GRUB2 bootloader"
arch=('x86_64')
url='https://invent.kde.org/system/kcm-grub2'
license=('GPL3')
depends=(
    'grub'
    'hwinfo'
    'kcmutils'
    'libmagick6'
    'packagekit-qt5'
)
makedepends=(
    'cmake'
    'extra-cmake-modules'
    'git'
    'kdoctools'
    'ninja'
)

conflicts=('grub2-editor-frameworks')
provides=('grub2-editor-frameworks')
optdepends=('os-prober: To detect other OSes when generating grub.cfg in BIOS systems')
source=("${_product}"::"git+${url}.git")
sha256sums=('SKIP')

pkgver() {
  cd "${_product}"
  # cutting off 'v' prefix that presents in the git tag
  git describe --long --tags | sed 's/^v//;s/\([^-]*-g\)/r\1/;s/-/./g'
}

prepare() {
   export PKG_CONFIG_PATH='/usr/lib/imagemagick6/pkgconfig'
   cmake -B build -S "${_product}" \
    -G Ninja \
    -D BUILD_TESTING=OFF \
    -Wno-dev
}

build() {
   cmake --build build
}

package() {
	 DESTDIR="${pkgdir}" cmake --install build
}
