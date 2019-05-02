from wsme.exc import MissingArgument as B
def A(funcdef,args,kw):
	'Check if some arguments are missing';assert len(args)==0
	for A in funcdef.arguments:
		if A.mandatory and A.name not in kw:raise B(A.name)