from __future__ import absolute_import
B=None
from django.core.urlresolvers import reverse as C
from slacker.django_backend.conf import SLACKER_SERVER as D
from .http import HttpWorker as A
class E(A):
	" HttpWorker with django's defaults "
	def __init__(F,server=B,path=B):B=path;A=server;A=A or D;B=B or C('slacker-execute');super(E,F).__init__(A,B)