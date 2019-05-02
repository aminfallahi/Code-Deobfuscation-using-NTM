from django import template as A
B=A.Library()
@B.inclusion_tag('tidings/email/unsubscribe.ltxt')
def C(watch):'Return instructions and link for unsubscribing from the given watch.';return{'watch':watch}