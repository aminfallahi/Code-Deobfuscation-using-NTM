import rasterio as A
from scipy.signal import medfilt as C
D='tests/data/RGB.byte.tif'
E='/tmp/filtered.tif'
with A.open(D)as B:F=B.read();G=B.profile
H=C(F,(1,5,5)).astype('uint8')
with A.open(E,'w',**G)as I:I.write(H)