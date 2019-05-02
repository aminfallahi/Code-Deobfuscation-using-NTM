_A='sample'
from projectname.tests import *
class TestSample2Controller(TestController):
	def test_session(self):B='session_increment';A='counter';response=self.app.get(url(controller=_A,action=B));assert response.session.has_key(A);assert response.session[A]==0;response=self.app.get(url(controller=_A,action=B));assert response.session[A]==1;assert'session incrementer'in response
	def test_default(self):response=self.app.get(url(controller=_A,action='test_template_caching'));assert'Hi everyone!'in response