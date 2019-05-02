__author__='pauloalmeida'
from skimage.io import imread as B
from skimage.filters import threshold_adaptive as C
import matplotlib.pyplot as A
class D:
	@staticmethod
	def adaptive_threshold(filename_in,filename_out):D=B(filename_in,as_grey=True);E=C(D,40,offset=10);A.imsave(filename_out,E,cmap=A.cm.gray)