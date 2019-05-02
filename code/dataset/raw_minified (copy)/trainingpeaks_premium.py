from django.shortcuts import render as D
from django.views.decorators.csrf import csrf_exempt as A
from django.utils.http import urlencode
@A
def B(request):
	F='personId';E='username';C='password';A=request;B={}
	if C in A.POST:B={C:A.POST[C],E:A.POST[E],F:A.POST[F]}
	return D(A,'trainingpeaks_premium.html',B)