from gluon import current as B
def A():
	'\n\t\tDefines the Organisations and branches for which the role test data is to be created.\n\t';D=None;C=['Org-A','Org-B','Org-C']
	if B.deployment_settings.get_org_branches():A=[D,'Branch-A']
	else:A=[D]
	return C,A