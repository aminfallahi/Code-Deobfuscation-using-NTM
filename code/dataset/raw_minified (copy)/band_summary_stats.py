from pprint import pprint as C
import rasterio as D,numpy as E
F='tests/data/RGB.byte.tif'
with D.open(F)as G:H=G.read()
B=[]
for A in H:B.append({'min':A.min(),'mean':A.mean(),'median':E.median(A),'max':A.max()})
C(B)