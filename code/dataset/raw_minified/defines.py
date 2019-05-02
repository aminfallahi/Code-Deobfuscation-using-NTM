'\nProject definitions\n'
import os
from gitver.git import project_root as B
A=B()
C='.gitver'
D=os.path.join(A,C)
E=os.path.join(D,'config')
F=os.path.join(A,'.gitignore')