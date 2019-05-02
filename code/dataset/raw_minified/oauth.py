from django.conf import settings as B
from django.template import Library as C
from ..utils import get_oauth_handler as D,get_gravatar_url as E
A=C()
@A.simple_tag
def F():A=D();return A.authorize_url(B.GITHUB['SCOPES'])
@A.simple_tag
def G(email,size):return E(email,size)