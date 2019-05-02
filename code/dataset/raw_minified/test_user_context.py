import jedi
def A():A='\x0c\nclass Test(object):\n    pass';jedi.Script(A,line=2,column=18).call_signatures()