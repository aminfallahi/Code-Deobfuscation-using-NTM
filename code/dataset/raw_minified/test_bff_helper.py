'\nCreated on Apr 8, 2011\n\n@organization: cert.org\n'
import unittest as A,os
class B(A.TestCase):
	def delete_file(A,f):os.remove(f);A.assertFalse(os.path.exists(f))
if __name__=='__main__':A.main()