import glob,unittest as A
B=glob.glob('*_test*.py')
C=[str[0:len(str)-3]for str in B]
D=[A.defaultTestLoader.loadTestsFromName(str)for str in C]
E=A.TestSuite(D)
F=A.TextTestRunner().run(E)