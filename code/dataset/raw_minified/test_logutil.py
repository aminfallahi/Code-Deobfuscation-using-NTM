import unittest as A,doctest as B,googkit.lib.logutil
def C(loader,tests,ignore):A=tests;A.addTests(B.DocTestSuite(googkit.lib.logutil));return A
if __name__=='__main__':A.main()