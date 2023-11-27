# Maintainer: Jakob Gahde <j5lx@fmail.co.uk>

_pkgname=edi
pkgname=${_pkgname}-git
pkgver=v0.8.0.28.ge9d30f6
pkgrel=1
pkgdesc="The EFL IDE"
arch=('i686' 'x86_64')
url="https://phab.enlightenment.org/w/projects/${_pkgname}/"
license=('GPL2')
depends=('efl' 'clang' 'check')
makedepends=('git' 'meson')
source=("git+https://git.enlightenment.org/enlightenment/edi.git")
md5sums=('SKIP')

pkgver() {
  cd "${srcdir}/${_pkgname}"
  echo $(git describe --always | sed 's/-/./g')
}

build() {
 arch-meson $_pkgname build \
   -Dlibclang=true
 ninja -C build
}

#check() {
#  cd "${srcdir}/${_pkgname}"
#
#  make check
#}

package() {
  DESTDIR=${pkgdir} ninja -C build install
}
