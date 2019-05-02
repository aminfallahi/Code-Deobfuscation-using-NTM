import unittest as A,doctest as B,googkit.lib.strutil
def C(loader,tests,ignore):A=tests;A.addTests(B.DocTestSuite(googkit.lib.option_builder));return A
if __name__=='__main__':A.main()