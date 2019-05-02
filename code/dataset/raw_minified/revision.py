from django import template as A
from django.core.cache import cache
B=A.Library()
@B.simple_tag
def C():
	A=cache.get('current_revision')
	if A==None:from lib.revision_hook import get_revision as B,set_cache as C;A=B();C(A)
	return 'Revision: <a href="https://github.com/upTee/upTee/commit/{0}">{1}</a>'.format(A,A[:7])