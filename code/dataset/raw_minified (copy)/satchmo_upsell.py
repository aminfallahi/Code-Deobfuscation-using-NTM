from django import template as A
B=A.Library()
def C(product):
	'\n    Display the list of products that are upsell candidates for currently viewed product.\n    ';A=product;B=None
	if A.upselltargets.count()>0:B=A.upselltargets.all()
	return{'goals':B}
B.inclusion_tag('upsell/product_upsell.html',takes_context=False)(C)