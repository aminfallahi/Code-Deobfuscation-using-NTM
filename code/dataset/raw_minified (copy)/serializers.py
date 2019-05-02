from rest_framework.serializers import ModelSerializer as A
from versatileimagefield.serializers import VersatileImageFieldSerializer as B
from .models import VersatileImageTestModel as C
class D(A):
	'Serializes VersatileImageTestModel instances';image=B(sizes='test_set')
	class Meta:model=C;fields='image',