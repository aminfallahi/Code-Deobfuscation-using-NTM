import unittest as B,lcs as A
class C(B.TestCase):
	def test_lcs(B):C='ABCD';B.assertEqual(A.longest_common_subsequence(C,'BBDABXYDCCAD'),(4,C));B.assertEqual(A.longest_common_subsequence('BANANA','ATANA'),(4,'AANA'));B.assertEqual(A.longest_common_subsequence('ABCDEFG','BDGK'),(3,'BDG'))
if __name__=='__main__':B.main()