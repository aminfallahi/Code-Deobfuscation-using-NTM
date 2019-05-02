from .main import Test
class A(Test):
	def TEMPLATE_CONTEXT_PROCESSORS(B):return tuple(super(A,B).TEMPLATE_CONTEXT_PROCESSORS())+('tests.settings.base.test_callback',)