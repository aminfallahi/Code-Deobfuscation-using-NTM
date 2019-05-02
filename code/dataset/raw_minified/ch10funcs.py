from osgeo import gdal
def A(fn):'Returns min_x, max_y, max_x, min_y';B=gdal.Open(fn);A=B.GetGeoTransform();return A[0],A[3],A[0]+A[1]*B.RasterXSize,A[3]+A[5]*B.RasterYSize