from django import template as A
B=A.Library()
@B.filter
def C(k,v):return k[v]