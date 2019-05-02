import api
def A():
	F='programming-language';E='/system-management/gentoo/abc';B='/programming-language'
	for A in [('/',[('index','/~index')]),(E,[('system-management','/system-management'),('gentoo','/system-management/gentoo'),('abc',E)]),(B,[(F,B)]),('/programming-language/',[(F,B)])]:C=A[0];D=A[1];assert api.zbox_wiki.mdutils.path2hierarchy(C)==D