# Contributor: micsproul at large search corporation's mail service.
# Contributor: Mohammad Alsaleh <msal@tormail.org>
# Maintainer: Steven Allen <steven@stebalien.com>

_date=2016-04-08
pkgname=rust-nightly-bin
pkgver=1.9.0_2016.04.07
pkgrel=1
arch=('i686' 'x86_64')
pkgdesc='Fast, concurrent, safe. The Rust programming language and its package manager, Cargo.'
url='http://www.rust-lang.org/'
license=('MIT' 'Apache' 'custom')
provides=('rust' 'rust-nightly' 'cargo' 'cargo-nightly')
conflicts=('rust' 'rust-git' 'rust-nightly' 'cargo-nightly-bin' 'cargo' 'cargo-git' 'cargo-nightly' 'cargo-nightly-bin')
depends=('gcc-libs' 'zlib' 'sh')
source=("rust-nightly-${_date}-${CARCH}-unknown-linux-gnu.tar.gz.asc::http://static.rust-lang.org/dist/${_date}/rust-nightly-${CARCH}-unknown-linux-gnu.tar.gz.asc"
        "rust-nightly-${_date}-${CARCH}-unknown-linux-gnu.tar.gz::http://static.rust-lang.org/dist/${_date}/rust-nightly-${CARCH}-unknown-linux-gnu.tar.gz"
)
        
sha256sums=('SKIP' 'SKIP')
validpgpkeys=('108F66205EAEB0AAA8DD5E1C85AB96E6FA1BE5FE')
options=(staticlibs !strip)

pkgver() {
  cd ${srcdir}/rust-nightly-${CARCH}-unknown-linux-gnu
  ver="$(expr "$(cat version)" : '\(.*\)-nightly')"
  date="$(expr "$(cat version)" : '.* \(.*\))')"
  echo "${ver}_${date//\-/.}"
}

package() {
    # Rust, Cargo and Documentation.
    cd rust-nightly-${CARCH}-unknown-linux-gnu
    ./install.sh \
        --disable-ldconfig \
        --destdir="${pkgdir}" \
        --prefix=/usr/

    install -dm755 "${pkgdir}/usr/share/bash-completion/"
    mv "${pkgdir}/usr/etc/bash_completion.d/" "${pkgdir}/usr/share/bash-completion/completions/"
    rmdir "${pkgdir}/usr/etc/"

    install -dm755 "${pkgdir}/usr/share/licenses/rust-nightly-bin/"{rust,cargo}

    mv "${pkgdir}"/usr/share/doc/cargo/LICENSE-* "${pkgdir}/usr/share/licenses/rust-nightly-bin/cargo/"
    mv "${pkgdir}"/usr/share/doc/rust/{LICENSE-*,COPYRIGHT} "${pkgdir}/usr/share/licenses/rust-nightly-bin/rust/"

    # Remove cruft.
    rm "${pkgdir}/usr/lib/rustlib/"{manifest-*,install.log,uninstall.sh,components,rust-installer-version}
}
