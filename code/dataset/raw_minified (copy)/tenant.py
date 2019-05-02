from django.template import Library as A
from django.template.defaulttags import url as C,URLNode as D
from tenant_schemas.utils import clean_tenant_url as E
F=A()
class B(D):
	def __init__(C,url_node):A=url_node;super(B,C).__init__(A.view_name,A.args,A.kwargs,A.asvar)
	def render(A,context):C=super(B,A).render(context);return E(C)
@F.tag
def G(parser,token):return B(C(parser,token))