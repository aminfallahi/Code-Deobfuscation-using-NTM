'Tests to ensure that the html.parser tree builder generates good\ntrees.'
from bs4.testing import SoupTest as A,HTMLTreeBuilderSmokeTest as B
from bs4.builder import HTMLParserTreeBuilder as C
class D(A,B):
	@property
	def default_builder(self):return C()
	def test_namespaced_system_doctype(A):0
	def test_namespaced_public_doctype(A):0