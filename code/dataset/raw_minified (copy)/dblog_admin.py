B=list
from django.contrib.admin.templatetags.admin_list import result_headers as C,items_for_result as D
from django import template as E
F=E.Library()
def G(cl):
	for A in cl.result_list:C=B(D(cl,A,None));(yield dict(cells=C,instance=A,num_real_cells=len(C)-1))
def A(cl):return{'cl':cl,'result_headers':B(C(cl)),'results':B(G(cl))}
A=F.inclusion_tag('admin/djangodblog/errorbatch/change_list_results.html')(A)