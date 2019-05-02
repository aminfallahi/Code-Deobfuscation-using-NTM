from __future__ import print_function
from pyshorteners import Shortener as B
def A():A=B('Tinyurl');print('\nHello World! Testing TinyurlShortener with www.google.com URL\nShorten url: {}\nExpanded: {}\n    '.format(A.short('http://www.google.com'),A.expand('http://goo.gl/fbsS')))
if __name__=='__main__':A()