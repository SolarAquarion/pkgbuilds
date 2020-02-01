# Maintainer: Maxime Gauduin <alucryd@archlinux.org>
# Contributor: Ner0 <darkelfdarkelf666@yahoo.co.uk>

pkgname=pantheon-files-git
pkgver=r6554.35b7661f
pkgrel=1
pkgdesc='The Pantheon File Browser'
arch=(x86_64)
url=https://github.com/elementary/files
license=(GPL3)
groups=(pantheon-unstable)
depends=(
  atk
  cairo
  gdk-pixbuf2
  glib2
  gtk3
  libcanberra
  libgee
  libgit2-glib
  granite-git
  desktop-file-utils
  libnotify
  pango
  sqlite
  zeitgeist
  libcloudproviders
)
makedepends=(
  git
  gnome-common
  granite-git
  meson
  vala
)
optdepends=(
  'contractor-git: Various context menu entries'
  'gvfs: Cleaner devices section'
  'tumbler: Thumbnails generation'
)
provides=(pantheon-files)
conflicts=(pantheon-files)
source=(pantheon-files::git+https://github.com/elementary/files.git)
sha256sums=(SKIP)

pkgver() {
  cd pantheon-files

  echo "r$(git rev-list --count HEAD).$(git rev-parse --short HEAD)"
}

build() {
  arch-meson pantheon-files build \
    -D with-unity=false
  ninja -C build
}

package() {
  DESTDIR="${pkgdir}" ninja -C build install
}

# vim: ts=2 sw=2 et:
