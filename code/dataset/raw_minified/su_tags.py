from django import template as A
from ..utils import su_login_callback as B
C=A.Library()
@C.inclusion_tag('su/login_link.html',takes_context=False)
def D(user):return{'can_su_login':B(user)}