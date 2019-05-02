import os,unittest as A,netCDF4 as B
class test_filepath(A.TestCase):
	def setUp(A):A.netcdf_file=os.path.join(os.getcwd(),'netcdf_dummy_file.nc');A.nc=B.Dataset(A.netcdf_file)
	def test_filepath(A):assert A.nc.filepath()==str(A.netcdf_file)
if __name__=='__main__':A.main()