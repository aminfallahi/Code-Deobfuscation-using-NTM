import sublime as D
def A():
	H='r extended';G='syntax_map';F='SublimeLinter.sublime-settings';E='user';A=D.load_settings(F)
	if A.has(E):
		B=A.get(E);C=B.get(G,{})
		if H not in C:C.update({H:'r'});B[G]=C;A.set(E,B);D.save_settings(F)