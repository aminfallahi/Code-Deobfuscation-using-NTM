from cafe.drivers.unittest.fixtures import BaseTestFixture as A
from cloudcafe.identity.composites import IdentityServiceComposite as B,AdminIdentityServiceComposite as C
class D(A):
	@classmethod
	def setUpClass(A):super(D,A).setUpClass();A.user_identity=B();A.user_identity.authenticate();A.user_identity.load_extensions();A.admin_identity=C();A.admin_identity.authenticate();A.admin_identity.load_extensions()