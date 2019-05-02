import unittest as A,os,sys,glob
if __name__=='__main__':
	B=os.path.dirname(__file__);C=glob.glob(os.path.join(B,'test_*.py'));D=[os.path.splitext(os.path.basename(str))[0]for str in C];E=[A.defaultTestLoader.loadTestsFromName(str)for str in D];F=A.TestSuite(E);G=A.TextTestRunner().run(F)
	if not G.wasSuccessful():sys.exit(1)