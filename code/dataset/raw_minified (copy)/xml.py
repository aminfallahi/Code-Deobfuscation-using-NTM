def A(context,func,args=[],kwargs={}):
	B=context
	for (C,A) in B:
		func(A,*args,**kwargs);A.clear()
		while A.getprevious()is not None:del A.getparent()[0]
	del B