'Release information.'
D='final'
C=str
from collections import namedtuple as B
A=B('version_info',('major','minor','micro','releaselevel','serial'))(1,0,0,D,1)
E='.'.join([C(B)for B in A[:3]])+(A.releaselevel[0]+C(A.serial)if A.releaselevel!=D else'')
F=B('Author',['name','email'])('Alice Bevan-McGregor','alice@gothcandy.com')
G='Turn any callable into a powerful command line script through arglist introspection.'
H='https://github.com/marrow/script/'