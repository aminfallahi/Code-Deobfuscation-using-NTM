import sublime,sublime_plugin as A
class B(A.TextCommand):
	def run(A,edit):
		for B in A.view.sel():
			if B.empty():C=A.view.line(B);D=A.view.substr(C)+'\n';A.view.insert(edit,C.begin(),D)
			else:A.view.insert(edit,B.begin(),A.view.substr(B))