
#!/usr/bin/python

# Created For SolusOS

from pisi.actionsapi import shelltools, get, autotools, pisitools


def setup():
	autotools.configure ()
						
def build():
	autotools.make ()
	
def install():
	autotools.install ()
	pisitools.dodoc ("COPYING", "AUTHORS", "ChangeLog")
