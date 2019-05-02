from decimal import Decimal as A
from market.models import Price,PriceCurrency as B
def C():
	E='0';C=Price.objects.create(name='Tier 0',price=A(E),active=True)
	for D in ['CAD','EUR','GBP','JPY']:B.objects.create(tier=C,price=A(E),currency=D)