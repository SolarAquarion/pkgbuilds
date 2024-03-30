# Merged with official ABS calligra PKGBUILD by João, 2021/05/30 (all respective contributors apply herein)
# Maintainer: João Figueiredo & chaotic-aur <islandc0der@chaotic.cx>
# Maintainer: Solomon Choina <shlomochoina@gmail.com

pkgname=calligra-git
pkgdesc="A set of applications for productivity and creative usage"
pkgver=3.3.89_r102357.g20eec562
pkgrel=2
arch=($CARCH)
url='https://www.calligra-suite.org/'
license=(FDL1.2 GPL2 LGPL)
depends=(cauchy gcc-libs glibc gsl imath kactivities5 kcontacts5 kcoreaddons5 kdelibs4support-git kdiagram5 kcmutils5 kinit knotifyconfig5 kross kwidgetsaddons5 libodfgen libspnav poppler-qt5 qca-qt5 qt5-base)
makedepends=(git boost eigen extra-cmake-modules-git kcalendarcore5 kdesignerplugin-git kdoctools5 libakonadi5 libetonyek libgit2 libvisio libwpg libwps marble-common-git pstoedit vc)
optdepends=('kirigami2-git: for Calligra Gemini'
            'libetonyek: Apple Keynote import filter'
            'libgit2: Calligra Gemini git plugin'
            'libvisio: Microsoft Visio import filter'
            'libwpg: Corel WordPerfect Graphics image importer'
            'libwps: Microsoft Works file word processor format import'
            'poppler: PDF to SVG filter'
            'pstoedit: EPS to SVG filter'
            'qt5-quickcontrols: for Calligra Gemini'
            'qt5-webengine: for Calligra Gemini')
conflicts=(${pkgname%-git})
provides=(${pkgname%-git})
source=("git+https://github.com/KDE/${pkgname%-git}.git"
        calligra-openexr3.patch
        068cd9ae.patch
        2ac46db5.patch
        62f51070.patch)
sha256sums=('SKIP'
            '96fbe4f06bf184e60ff653a1574f0f0523af5b4672ced2a501cd54642961dffe'
            '4516d15421209e5d8c8b5008140dbcb1eefa96b0e96e0da49b343e1799a8cefd'
            'c88e6d7a1f67c1b5413b624aa67fca2841205fdf4201f6682f69bae737582922'
            '8a94e076c09887ff0741da3276ce4652063351b884c66d4c9ba0cde431dbb867')


prepare() {
  patch -d $pkgname-$pkgver -p1 < calligra-openexr3.patch # Fix build with OpenEXR 3
  patch -d $pkgname-$pkgver -p1 < 068cd9ae.patch # Remove dynamic exception specifications
  patch -d $pkgname-$pkgver -p1 < 2ac46db5.patch # Prerequisite for the following patch
  patch -d $pkgname-$pkgver -p1 < 62f51070.patch # Fix fontconfig linking
}

pkgver() {
  cd ${pkgname%-git}
  _ver="$(grep -m1 'set(CALLIGRA_VERSION_STRING' CMakeLists.txt | cut -d '"' -f2 | tr - .)"
  echo "${_ver}_r$(git rev-list --count HEAD).g$(git rev-parse --short HEAD)"
}

build() {
  cmake -B build -S ${pkgname%-git} \
    -DQT_MAJOR_VERSION=6 \
    -DBUILD_TESTING=OFF
  cmake --build build
}

package() {
  DESTDIR="$pkgdir" cmake --install build

# Remove utterly broken thumbnailers
  rm "$pkgdir"/usr/lib/qt/plugins/calligra*thumbnail.so
}
