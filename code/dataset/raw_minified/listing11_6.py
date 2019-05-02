import os,scipy.ndimage
from osgeo import gdal as B
import ospybook as C
D='D:\\osgeopy-data\\Nepal\\everest.tif'
E='D:\\Temp\\everest_smoothed.tif'
A=B.Open(D)
F=A.GetRasterBand(1).ReadAsArray()
G=scipy.ndimage.filters.uniform_filter(F,size=3,mode='nearest')
C.make_raster(A,E,G,B.GDT_Int32)
del A