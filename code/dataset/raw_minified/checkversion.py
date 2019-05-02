import netCDF4 as B,sys as A,numpy
A.stdout.write('netcdf4-python version: %s\n'%B.__version__)
A.stdout.write('HDF5 lib version:       %s\n'%B.__hdf5libversion__)
A.stdout.write('netcdf lib version:     %s\n'%B.__netcdf4libversion__)
A.stdout.write('numpy version           %s\n'%numpy.__version__)