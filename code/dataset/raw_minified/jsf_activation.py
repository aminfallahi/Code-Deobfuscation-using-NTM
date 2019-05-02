import os
def A(view):
	G='json';F=None;B=view.file_name();E=view.settings();C=E.get('syntax');A='';D=''
	if B!=F:D=os.path.splitext(B)[1][1:]
	if C!=F:A=os.path.splitext(C)[0].split('/')[-1].lower()
	return D in['js',G]or'javascript'in A or G in A