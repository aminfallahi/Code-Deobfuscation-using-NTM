from mkt.collections.models import Collection as A
def B():
	'Backfill slugs.'
	for B in A.objects.all():B.save()