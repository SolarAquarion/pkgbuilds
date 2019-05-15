  # Maintainer:  solaraquarion <shlomochoina@gmial.com>
pkgname=extraterm-bin
_pkgname=extraterm
pkgver=0.42.1
pkgrel=1
conflicts=("extraterm")
pkgdesc="The swiss army chainsaw of terminal emulators."
arch=("x86_64")
url="https://github.com/sedwards2009/extraterm"
license=("MIT")
depends=("nodejs")
source=("$url/releases/download/v$pkgver/extraterm-$pkgver-linux-x64.zip")
sha256sums=('8f03bca962b1dbbc2a7ed9a15cdb04629e763ebf037d10b2ea8d35018d5974d6')

package() {
  cd $srcdir

  install -d $pkgdir/opt
  install -d $pkgdir/opt/$_pkgname

  install -d $pkgdir/usr/bin
  cp -r "$srcdir/$_pkgname-$pkgver-linux-x64"/* "$pkgdir/opt/$_pkgname"

   install -Dm755 /dev/stdin "$pkgdir"/usr/bin/$_pkgname <<END
#!/usr/bin/bash
/opt/extraterm/extraterm
END

  local _icon_dir="usr/share/icons/hicolor"
  install -Dm644 $pkgdir/opt/$_pkgname/resources/app/extraterm/resources/logo/extraterm_main_logo.svg $pkgdir/$_icon_dir/scalable/apps/$_pkgname.svg

   install -Dm644 $pkgdir/opt/$_pkgname/resources/app/extraterm/resources/logo/extraterm_small_logo_256x256.png  $pkgdir/$_icon_dir/256x256/apps/$_pkgname.png

  install -Dm644 $pkgdir/opt/$_pkgname/resources/app/extraterm/resources/extraterm.desktop $pkgdir/usr/share/applications/extraterm.desktop

  install -Dm755 $pkgdir/opt/$_pkgname/LICENSE.txt $pkgdir/usr/share/licenses/$_pkgname/copyright
}
