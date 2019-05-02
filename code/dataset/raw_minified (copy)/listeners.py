import logging as A
C=A.getLogger('wishlist.listener')
def B(sender,request=None,method={},**E):
	'Listens for cart_add_view signal and checks to see if it is a wishlist add request.\n    If so, returns the wishlist add view method.\n    ';B='';A=request
	if A and A.method=='POST':
		if A.POST.get('addwish',B)!=B or A.POST.get('addwish.x',B)!=B:C.debug('Found addwish in post, returning the wishlist add view');from satchmo_ext.wishlist.views import wishlist_add as D;method['view']=D