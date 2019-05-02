E=print
import sys
if sys.version_info<(3,0):from urllib2 import urlopen
else:from urllib.request import urlopen
import io
from colorthief import ColorThief as B
C=urlopen('http://lokeshdhakar.com/projects/color-thief/img/photo1.jpg')
D=io.BytesIO(C.read())
A=B(D)
E(A.get_color(quality=1))
E(A.get_palette(quality=1))