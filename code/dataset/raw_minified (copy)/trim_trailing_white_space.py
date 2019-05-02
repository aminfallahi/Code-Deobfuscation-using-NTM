D=True
import sublime,sublime_plugin as A
class B(A.EventListener):
	def on_pre_save(F,view):
		A=view
		if A.settings().get('trim_trailing_white_space_on_save')==D:
			B=A.find_all('[\t ]+$');B.reverse();C=A.begin_edit()
			for E in B:A.erase(C,E)
			A.end_edit(C)
class C(A.EventListener):
	def on_pre_save(E,view):
		C='\n';A=view
		if A.settings().get('ensure_newline_at_eof_on_save')==D:
			if A.size()>0 and A.substr(A.size()-1)!=C:B=A.begin_edit();A.insert(B,A.size(),C);A.end_edit(B)