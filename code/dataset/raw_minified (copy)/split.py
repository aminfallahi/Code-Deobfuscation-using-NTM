from django import template as A
B=A.Library()
@B.filter
def C(str,splitter):return str.split(splitter)