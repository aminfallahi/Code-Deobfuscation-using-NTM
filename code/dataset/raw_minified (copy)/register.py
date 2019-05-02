E='README.txt'
D=open
import pandoc as A,os
A.core.PANDOC_PATH='/usr/local/bin/pandoc'
B=A.Document()
B.markdown=D('README.md').read()+D('HISTORY.md').read()
C=D(E,'w+')
C.write(B.rst)
C.close()
os.system('python setup.py register')
os.remove(E)