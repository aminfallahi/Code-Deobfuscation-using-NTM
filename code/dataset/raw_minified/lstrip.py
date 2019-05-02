from suplemon.suplemon_module import Module as A
class B(A):
	def run(E,app,editor,args):
		A=editor;C=A.get_lines_with_cursors()
		for D in C:B=A.lines[D];B.data=B.data.lstrip()
C={'class':B,'name':'lstrip'}