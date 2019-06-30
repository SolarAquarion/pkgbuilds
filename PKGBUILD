# Maintainer: Solomon Choina <shlomochoina@gmail.com>
pkgname=libgnt3-hg
pkgver=r1337.04d9c8e5cb95
epoch=1
pkgrel=1
pkgdesc="The GLib Ncurses Toolkit"
arch=('x86_64')
url="https://bitbucket.org/pidgin/libgnt"
license=('GPL3')
depends=('glib2' 'ncurses' 'libxml2' 'python')
makedepends=('mercurial' 'meson' 'libxml2' 'python' 'gobject-introspection' 'gtk-doc')
provides=("${pkgname%-VCS}")
conflicts=("${pkgname%-VCS}")
source=('hg+https://bitbucket.org/pidgin/libgnt#branch=default')
sha256sums=('SKIP')

pkgver() {
	cd "$srcdir/${pkgname%3-hg}"

	printf "r%s.%s" "$(hg identify -n)" "$(hg identify -i)"
}

build() {
	arch-meson libgnt build
  ninja -C build
}

#check() {
#	make -k check
#}

package() {
	DESTDIR="$pkgdir/" ninja -C build install
}
