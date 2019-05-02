from django import template as A
B=A.Library()
@B.filter('field_type')
def C(obj):return obj.__class__.__name__