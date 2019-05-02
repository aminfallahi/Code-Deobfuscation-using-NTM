'\nDEPRECATED; To be removed in 1.0\n'
from __future__ import absolute_import
import rasterio.mask
def A(*A,**B):import warnings as C;C.warn('Deprecated; Use rasterio.mask instead',DeprecationWarning);return rasterio.mask.mask(*A,**B)