from models import BillingCycle as C
def A():
	A=[];D=C.objects.filter(bill__reminder_count=2,membership__status='A',is_paid=False)
	for E in D:
		B=E.membership;F=B.alias_set.filter(account=True)
		for G in F:A.append((B.id,G.name))
	return A