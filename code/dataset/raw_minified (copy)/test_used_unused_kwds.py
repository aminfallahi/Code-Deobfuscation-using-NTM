__author__="Brian O'Neill"
__version__='0.2.4'
from log_calls import used_unused_kwds as A
from log_calls.used_unused_kwds import used_unused_keywords
import doctest as B,unittest
def C(loader,tests,ignore):C=tests;C.addTests(B.DocTestSuite(A));return C
if __name__=='__main__':B.testmod(A)