from django import template as B
A=B.Library()
def C(address):'Output an address as a HTML formatted text block';return{'address':address}
A.inclusion_tag('contact/_addressblock.html')(C)
def D(user):
	A=user
	if not A.is_anonymous()and A.contact_set.count()>0:return A.contact_set.all()[0]
	return None
A.filter('contact_for_user')(D)