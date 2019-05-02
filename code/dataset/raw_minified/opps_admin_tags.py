from django import template as A
B=A.Library()
@B.simple_tag
def C(obj,url=None):A=url;A=A or'';return A.format(obj=obj)