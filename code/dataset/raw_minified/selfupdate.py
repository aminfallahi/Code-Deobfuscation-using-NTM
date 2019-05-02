import os,logger as A,subprocess as B
def C(repository_path):
	os.chdir(repository_path);C=B.check_output(['git','pull','--all'])
	for D in C.splitlines():A.instance.debug(D)