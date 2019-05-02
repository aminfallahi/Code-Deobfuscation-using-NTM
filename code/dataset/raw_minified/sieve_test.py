import unittest as A
from sieve_of_eratosthenes import calculate_primes as B
class C(A.TestCase):
	def test_primes(A):A.prime_list=[2,3,5,7,11,13,17,19];A.assertEqual(A.prime_list,B(20))
if __name__=='__main__':A.main()