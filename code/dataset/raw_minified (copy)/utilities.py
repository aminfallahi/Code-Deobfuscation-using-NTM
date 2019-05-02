'Test helpers.'
D='\n'
def A(text,tabs=None,end=D):
	'Strip leading whitespace indentation on multiline string literals.';E=' ';A=tabs;B=[]
	for C in text.strip().splitlines():
		if not A:A=C.count(E*4)
		B.append(C.replace(E*A*4,'',1))
	return D.join(B)+end