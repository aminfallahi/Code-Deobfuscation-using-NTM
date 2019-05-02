'\nUse the unittest framework to execute the same tests as in test.py, \nTest succeeds in unittest if pmt.py command returns success status to shell\nSo this test succeeds if pmt runs and does not crash, \neven if pmt reports PyModel test failed.\n'
import unittest as A,os
class B(A.TestCase):
	def test_n6(A):'pmt -n 6 populations, no seed so different test run each time';B=os.system('pmt -n 6 populations');A.assertEqual(B,0)
if __name__=='__main__':A.main()