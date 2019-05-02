from django import template as A
B=A.Library()
@B.filter
def C(value):A=value;return (A+A).upper()