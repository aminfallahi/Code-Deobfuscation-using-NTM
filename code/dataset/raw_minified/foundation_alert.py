from django import template as A
B=A.Library()
@B.inclusion_tag('foundation_alert/alert.html')
def C(message,css_class='success',is_close=True):'Render foundation alert box.';return{'message':message,'css_class':css_class,'is_close':is_close}