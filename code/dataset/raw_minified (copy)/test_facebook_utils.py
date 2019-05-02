'\nTesting Facebook Utils\n'
import unittest as A,os
from indico.utils.auth.facebook_utils import check_access_token as B
class C(A.TestCase):
	def test_access_token(A):A.assertTrue(B(os.environ.get('USER_SALT')));A.assertFalse(B('wrong_token'))
if __name__=='__main__':A.main()