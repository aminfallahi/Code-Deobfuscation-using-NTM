from django import template as A
from satchmo_utils.templatetags import get_filter_args
B=A.Library()
def C(order):'Output a formatted block giving attached gift certifificate details.';return{'order':order}
B.inclusion_tag('giftcertificate/_order_summary.html')(C)