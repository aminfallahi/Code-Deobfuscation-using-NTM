from distutils.core import setup
from source_module import cc
def A():setup(ext_modules=[cc.distutils_extension()])
if __name__=='__main__':A()