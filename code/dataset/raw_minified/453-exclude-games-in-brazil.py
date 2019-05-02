import mkt
from mkt.webapps.models import AddonExcludedRegion as C,Webapp as A
def B():
	'Exclude Games in Brazil.';B=A.category('games')
	if B:
		D=A.objects.filter(categories=B.id)
		for E in D:C.objects.get_or_create(addon=E,region=mkt.regions.BR.id)