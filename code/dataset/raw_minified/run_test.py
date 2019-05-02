import os,netCDF4 as B
A='http://geoport-dev.whoi.edu/thredds/dodsC/estofs/atlantic'
C=B.Dataset(A)
assert C.filepath()==A
D=os.path.join(os.environ['SRC_DIR'],'test')
os.chdir(D)
os.system('python run_all.py')