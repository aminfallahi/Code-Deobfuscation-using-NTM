D=open
import pandoc as A,os
A.core.PANDOC_PATH=os.environ['PANDOC_HOME']
B=A.Document()
B.markdown=D('README.md').read()
C=D('README.txt','w+')
C.write(B.rst)
C.close()