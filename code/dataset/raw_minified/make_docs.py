G='docs'
import os,subprocess as D,shutil
E='sphinx-build'
A='build/doctrees'
B=G
for C in (A,B):
	if not os.path.exists(C):os.makedirs(C)
open(os.path.join(B,'.nojekyll'),'w').close()
F=D.call([E,'-d',A,'-b','html','.',G])
raise SystemExit(F)