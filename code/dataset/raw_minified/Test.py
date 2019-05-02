import unittest as A
from pi3d.loader.parse_mtl_test import ParseMtlTest as B
def C():C=A.TestLoader().loadTestsFromTestCase(B);return C
if __name__=='__main__':A.TextTestRunner().run(C())