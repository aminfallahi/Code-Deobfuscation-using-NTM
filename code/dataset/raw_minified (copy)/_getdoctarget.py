import py
def get_version_string():
	A='..';fn=py.path.local(__file__).join(A,A,A,'_pytest','__init__.py')
	for line in fn.readlines():
		if'version'in line and not line.strip().startswith('#'):return eval(line.split('=')[-1])
def get_minor_version_string():A='.';return A.join(get_version_string().split(A)[:2])
if __name__=='__main__':print(get_minor_version_string())