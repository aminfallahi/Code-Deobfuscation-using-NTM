import affine as B,numpy,rasterio as C
def A():D=numpy.ones((10,10));E=B.Affine(1.0,0.0,0.0,0.0,-1.0,10.0);F,A=C.pad(D,E,2,'edge');assert F.shape==(14,14);assert A.xoff==-2.0;assert A.yoff==12.0