# Maintainer: Thomas Adam <thomas@fvwm.org>
# Maintainer: boonpatrol

pkgname=fvwm3
pkgver=1.0.6a
pkgrel=1
pkgdesc="A highly customizable virtual desktop window manager with small memory footprint."
arch=('x86_64')
url="https://www.fvwm.org"
license=('GPL' 'custom')
depends=('libevent' 'libx11' 'libxft' 'libxrender' 'libxt' 'python' 'libxrandr' )
provides=('fvwm=3')
conflicts=('fvwm')
makedepends=('libxslt' 'asciidoctor')
optdepends=('fontconfig'
            'freetype2'
            'fribidi'
            'ncurses'
            'libpng'
            'readline'
            'librsvg'
            'libsm'
            'libxcursor'
            'libxext'
            'libxi'
            'libxpm'
            'sharutils' )
options=('!emptydirs' '!makeflags')
source=("https://github.com/fvwmorg/fvwm3/releases/download/${pkgver}/fvwm3-${pkgver}.tar.gz" 'fvwm3.desktop')
sha256sums=('4665a66133e070b791917b0794cc6df6b754679ebe9130718427db6479bb5b68'
            'e18c21b37219328309ac97b0026778299fc5db8d4aec3a4610287d92cec260db')

build() {
  cd "${pkgname}-${pkgver}"
  ./configure --prefix=/usr \
              --sysconfdir=/etc \
              --libexecdir=/usr/lib \
              --enable-mandoc
  make
}

package() {
  cd "${pkgname}-${pkgver}"
  make DESTDIR="${pkgdir}/" install
  install -d "${pkgdir}/usr/share/doc/fvwm3"
  install -D -m644 ../fvwm3.desktop "${pkgdir}/usr/share/xsessions/fvwm3.desktop"
  install -D -m644 COPYING "${pkgdir}/usr/share/licenses/${pkgname}/COPYING"
}
