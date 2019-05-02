import django_filters as A
from enhanced_cbv.tests.models import Author as B
class C(A.FilterSet):
	class Meta:model=B;fields=['name']