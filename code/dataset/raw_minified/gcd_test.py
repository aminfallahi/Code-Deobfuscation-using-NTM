import unittest as C,fractions as A,GCD as B
class D(C.TestCase):
	def test_gcd(C):C.assertEqual(A.gcd(30,50),B.greatest_common_divisor(30,50));C.assertEqual(A.gcd(55555,123450),B.greatest_common_divisor(55555,123450));C.assertEqual(A.gcd(-30,-50),B.greatest_common_divisor(-30,-50));C.assertEqual(A.gcd(-1234,1234),B.greatest_common_divisor(-1234,1234))
if __name__=='__main__':C.main()