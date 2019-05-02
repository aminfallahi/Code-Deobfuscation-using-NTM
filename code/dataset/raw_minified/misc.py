'\nCreated on Oct 24, 2012\n\n@organization: cert.org\n'
def A(module,api_list):
	B=module;A=[]
	for C in api_list:
		if not hasattr(B,C):A.append((B.__name__,C))
	D=['API missing: %s.%s not found'%B for B in A];E='\n'.join(D);return bool(len(A)),E