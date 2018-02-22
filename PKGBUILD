# Contributor: micsproul at large search corporation's mail service.
# Contributor: Mohammad Alsaleh <msal@tormail.org>
# Maintainer: Steven Allen <steven@stebalien.com>

pkgname=rust-nightly-bin
pkgver=1.25.0_2018.02.18
pkgrel=1
arch=('i686' 'x86_64')
pkgdesc='Fast, concurrent, safe. The Rust programming language and its package manager, Cargo.'
url='https://www.rust-lang.org/'
license=('MIT' 'Apache' 'custom')
provides=('rust' 'rust-nightly' 'cargo' 'cargo-nightly' 'rust-docs')
conflicts=('rust' 'rust-git' 'rust-nightly' 'cargo-nightly-bin' 'cargo' 'cargo-git' 'cargo-nightly' 'cargo-nightly-bin' 'rust-docs')
depends=('gcc-libs' 'zlib' 'sh')
source=("rust-nightly-${pkgver}-${CARCH}-unknown-linux-gnu.tar.gz::https://static.rust-lang.org/dist/rust-nightly-${CARCH}-unknown-linux-gnu.tar.gz"
)

sha256sums=('SKIP')
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

    # Remove duplicate .so libraries and symlink to them.
    # https://github.com/rust-lang/rust/issues/37971
    find "${pkgdir}/usr/lib/rustlib/" -name "*.so" -exec ln -rfs -t "${pkgdir}/usr/lib/" {} +
}
