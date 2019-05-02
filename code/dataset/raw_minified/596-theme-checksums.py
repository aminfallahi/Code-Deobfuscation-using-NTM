from addons.models import Persona as A
from addons.tasks import calc_checksum as B
from amo.utils import chunked as C
def D():
	'Calculate checksums for all themes.';D=A.objects.filter(checksum='').values_list('id',flat=True)
	for E in C(D,1000):[B.delay(A)for A in E]