# Maintainer: pavbaranov <pavbaranov at gmail dot com>
# Maintainer: Piotr Gorski <lucjan.lucjanov@gmail.com>
# Maintainer : Solomon Choina <shlomochoina@gmail.com>
pkgname=falkon-git
pkgver=3.0.1.160.g7b2ff160
pkgrel=1
pkgdesc="Cross-platform Qt Web Browser"
arch=('i686' 'x86_64')
url="http://www.qupzilla.com"
license=('GPL')
depends=('qt5-webengine' 'qt5-x11extras' 'qt5-svg' 'openssl>=1.1.0')  # 'python-pyside2-git' : uncomment if you want to enable experimental function for add new plugins)
makedepends=('git' 'qt5-tools' 'kwallet' 'extra-cmake-modules' 'libgnome-keyring' ) # uncomment 'shiboken2-git' 'pyside2-common-git' : if you want to enable experimental function for add new plugins) #libgnome-keyring : uncomment if you want to enable GNOME keyring
conflicts=('qupzilla' 'qupzilla-qt5' 'qupzilla-qt5-git' 'falkon')
optdepends=(
  'bash-completion: bash completion support'
  'kwallet: kf5 kwallet integration'
  'libgnome-keyring: gnome keyring integration'
  #'pyside2-common-git'
  #'shiboken2-git'
  )
source=("git+https://anongit.kde.org/falkon.git")
sha256sums=('SKIP')

pkgver() {
  cd "${pkgname%-*}"
  git describe --long --tags | sed 's/^v//;s/-/./g'
}

prepare(){
  mkdir -p build
  cd "${pkgname%-*}"
  sed -i 's/set(ENABLE_PYTHON_PLUGINS TRUE)//' CMakeLists.txt

}
build() {
  cd build
  cmake ../"${pkgname%-*}" \
    -DCMAKE_INSTALL_PREFIX=/usr \
    -DKDE_INSTALL_LIBDIR=lib \
    -DCMAKE_BUILD_TYPE=Release
  make
}

package() {
  cd build
  make DESTDIR="$pkgdir/" install
}
