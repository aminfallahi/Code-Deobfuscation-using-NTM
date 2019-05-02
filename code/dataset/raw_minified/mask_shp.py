import fiona,rasterio as B
from rasterio.tools.mask import mask
with fiona.open('tests/data/box.shp','r')as E:F=[A['geometry']for A in E]
with B.open('tests/data/RGB.byte.tif')as C:A,G=mask(C,F,crop=True);D=C.meta.copy()
D.update({'driver':'GTiff','height':A.shape[1],'width':A.shape[2],'transform':G})
with B.open('/tmp/masked.tif','w',**D)as H:H.write(A)