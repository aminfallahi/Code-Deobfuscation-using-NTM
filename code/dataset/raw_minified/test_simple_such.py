from nose2.tools import such
with such.A('system')as it:
	@it.should('do something')
	def test():0
it.createTests(globals())