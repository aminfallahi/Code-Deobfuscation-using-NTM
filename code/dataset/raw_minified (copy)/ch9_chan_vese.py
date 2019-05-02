from PIL import Image
from numpy import *
from scipy.misc import imsave
from PCV.tools import rof
'\nSimple example of Chan-Vese segmentation from Section 9.3.\nLoad an image, segment in two classes and save result.\n'
im=array(Image.open('../data/houses.png').convert('L'))
U,T=rof.denoise(im,im,tolerance=0.001)
t=0.4
imsave('result.pdf',U<t*U.max())