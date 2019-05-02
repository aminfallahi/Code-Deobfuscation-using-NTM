from rasterio.errors import NodataShadowWarning as A
def B():assert str(A())=="The dataset's nodata attribute is shadowing the alpha band. All masks will be determined by the nodata attribute"