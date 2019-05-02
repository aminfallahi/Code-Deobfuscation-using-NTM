D='id'
from tastypie.resources import ModelResource as A,ALL
from .models import Filer,Filing as C
from .utils.serializer import CIRCustomSerializer as B
class E(A):
	class Meta:queryset=Filer.objects.all();serializer=B();filtering={'filer_id_raw':ALL};excludes=[D]
class F(A):
	class Meta:queryset=C.objects.all();serializer=B();filtering={'filing_id_raw':ALL};excludes=[D]