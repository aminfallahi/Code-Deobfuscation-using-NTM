from amo.utils import chunked as A
from mkt.developers.tasks import generate_image_assets as B
from mkt.webapps.models import Webapp as C
def D():
	for D in A(C.objects.all(),50):
		for E in D:
			try:B.delay(E)
			except Exception:pass