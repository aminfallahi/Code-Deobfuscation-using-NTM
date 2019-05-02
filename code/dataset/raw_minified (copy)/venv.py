import os,tempfile as B
from plumbum import local
from plumbum.cmd import virtualenv as C
def D(tmp_dir=None):
	A=tmp_dir
	if not A:A=B.mkdtemp()
	C('--no-site-packages',A);return A
def A(package_name,venv_dir):
	A=venv_dir
	if not os.path.exists(A):A=D()
	B='%s/bin/pip'%A;local[B]('install',package_name)