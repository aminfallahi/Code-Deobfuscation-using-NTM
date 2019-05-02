_A='sample'
from projectname.tests import *
class TestSample2Controller(TestController):
	def test_session(self):B='session_increment';A='counter';response=self.app.get(url(controller=_A,action=B));assert response.session.has_key(A);assert response.session[A]==0;response=self.app.get(url(controller=_A,action=B));assert response.session[A]==1;assert'session incrementer'in response
	def test_genshi_default(self):self._test_genshi_default('testdefault')
	def _test_genshi_default(self,action):response=self.app.get(url(controller=_A,action=action));assert'Hello from Genshi'in response;assert'This is in c var'in response