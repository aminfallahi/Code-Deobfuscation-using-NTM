from django import template as A
B=A.Library()
@B.filter(name='get_item')
def C(dictionary,key):return getattr(dictionary,key)