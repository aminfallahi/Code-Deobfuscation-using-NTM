A=FreeDesktopPackage('%{name}','pkg-config','0.27',configure_flags=['--with-internal-glib'])
A.needs_lipo=True