B='html'
import os,conf
A='werkzeug-docs-'+conf.version
os.chdir('_build')
os.rename(B,A)
os.system('tar czf %s.tar.gz %s'%(A,A))
os.rename(A,B)