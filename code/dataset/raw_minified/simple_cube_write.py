E=True
from astropy.io import fits as A
from hyperion.model import ModelOutput as C
from hyperion.util.constants import pc
D=C('simple_cube.rtout')
B=D.get_image(inclination=0,distance=300*pc,units='MJy/sr')
A.writeto('simple_cube.fits',B.val.swapaxes(0,2).swapaxes(1,2),clobber=E)
A.writeto('simple_cube_slice.fits',B.val[:,:,1],clobber=E)