# Contributor: Laurent Carlier <lordheavym@gmail.com>
# Maintainer: Solomon Choina <shlomochoina@gmail.com>
pkgname=libclc-git
pkgver=17.0.0_r464818.04ed822dcc21
pkgrel=1
epoch=1
groups=('chaotic-mesa-git')
pkgdesc="Library requirements of the OpenCL C programming language (git version)"
arch=('i686' 'x86_64')
url="http://libclc.llvm.org/"
license=('MIT')
provides=('libclc')
conflicts=('libclc')
makedepends=('clang' 'llvm-libs' 'spirv-llvm-translator' 'polly' 'git' 'python' 'ninja' 'cmake')
source=('llvm-project-git::git+https://github.com/llvm/llvm-project.git')
md5sums=('SKIP')

pkgver() {
  cd llvm-project-git/llvm
  local _pkgver=$(awk -F 'MAJOR |MINOR |PATCH |)' \
          'BEGIN { ORS="." ; i=0 } \
           /set\(LLVM_VERSION_/ { print $2 ; i++ ; if (i==2) ORS="" } \
           END { print "\n" }' \
           CMakeLists.txt)_r$(git rev-list --count HEAD).$(git rev-parse --short HEAD)
  echo "${_pkgver}"

}

prepare() {
   cd llvm-project-git

  rm -rf build && mkdir build
}
build() {
  cd llvm-project-git/build

  export CXXFLAGS="${CXXFLAGS} -fno-lto"
  export CFLAGS="${CFLAGS} -fno-lto"


   cmake ../libclc -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DCMAKE_INSTALL_DATADIR=/usr/lib \
    -DLIBCLC_TARGETS_TO_BUILD="all"

    ninja all
}

package() {
  cd "$srcdir/llvm-project-git/libclc"

  DESTDIR="$pkgdir" ninja -C ../build install
  install -Dm644 LICENSE.TXT "$pkgdir/usr/share/licenses/$pkgname/LICENSE"
}
