C=True
from haystack import indexes as A
from mozdns.domain.models import Domain as B
class D(A.SearchIndex,A.Indexable):
	text=A.CharField(document=C,use_template=C);name=A.CharField(model_attr='name')
	def index_queryset(A):return A.get_model().objects.all()
	def get_model(A):return B