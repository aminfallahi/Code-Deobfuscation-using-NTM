from django.conf import settings
from django.core.exceptions import PermissionDenied as B
from django.core.paginator import Paginator as C,InvalidPage as D
from django.http import Http404 as E
def A(request,queryset,results_per_page=20):
	A=C(queryset,results_per_page)
	try:F=A.page(int(request.GET.get('page',1)))
	except D:raise E('Sorry, that page of results does not exist.')
	except ValueError:raise B()
	return F,A