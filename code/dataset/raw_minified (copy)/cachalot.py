from django.apps import apps
from django.template import Library as A
from ..api import get_last_invalidation as C
B=A()
@B.assignment_tag
def D(*D,**E):
	A=[]
	for B in D:
		if'.'in B:A.append(apps.get_model(B))
		else:A.append(B)
	return C(*A,**E)