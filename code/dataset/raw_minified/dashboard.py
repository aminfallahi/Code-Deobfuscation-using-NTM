from django.shortcuts import render as A
from django.views.decorators.csrf import ensure_csrf_cookie as B
@B
def C(req):return A(req,'dashboard.html')