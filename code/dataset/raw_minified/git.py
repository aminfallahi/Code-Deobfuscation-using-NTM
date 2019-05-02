import os,datetime as B,re
C=re.compile('Date:   (.*?) -?\\d+$',re.MULTILINE)
def A(gitPath):
	' Gets the timestamp of the last git commit.';os.chdir(gitPath);D=os.popen('%s rev-list HEAD --pretty --max-count=1'%os.environ['TM_GIT']);E=D.read();A=C.search(E)
	if A:return B.datetime.strptime(A.groups()[0],'%a %b %d %H:%M:%S %Y')