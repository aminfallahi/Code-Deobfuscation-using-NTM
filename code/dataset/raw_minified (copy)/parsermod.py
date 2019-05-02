from docutils.parsers import Parser as A
from docutils import nodes as B
class A(A):
	def parse(D,input,document):C='Generated section';A=B.section(ids=['id1']);A+=B.title(C,C);document+=A
	def get_transforms(A):return[]