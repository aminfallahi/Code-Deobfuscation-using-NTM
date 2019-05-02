import pprint as A,rasterio as B
from rasterio.features import shapes as C
with B.open('tests/data/shade.tif')as D:E=D.read(1)
A.pprint(list(C(E))[:2])