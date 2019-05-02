C=IOError
import os
try:from urllib import urlretrieve
except ImportError:from urllib.request import urlretrieve
def A(path,name,overwrite=False):
	'Check that path exists and is directory and that there is no file with\n    name in that directory. Then returns full path to file.\n    ';A=path;B=os.path.join(A,name)
	if not os.path.isdir(A):raise C('{} is not a directory or does not exist.'.format(A))
	if os.path.exists(B)and not overwrite:raise C('{} already exists in {}.'.format(name,A))
	return B