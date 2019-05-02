C=True
B='/bin/gcc --version'
import utils as A,utils as D
D.execute(B,shell=C)
A.execute(B,shell=C)
D.execute_with_timeout(B,shell=C)
A.execute_with_timeout(B,shell=C)
A.execute_with_timeout(['/bin/gcc','--version'],shell=False)