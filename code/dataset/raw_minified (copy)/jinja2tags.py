from __future__ import absolute_import,unicode_literals
import jinja2 as C
from jinja2.ext import Extension as B
from .templatetags.wagtailuserbar import wagtailuserbar as D
class A(B):
	def __init__(B,environment):super(A,B).__init__(environment);B.environment.globals.update({'wagtailuserbar':C.contextfunction(D)})
E=A