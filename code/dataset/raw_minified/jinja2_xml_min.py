from __future__ import absolute_import,division,print_function,unicode_literals
import re
from .  import jinja2_htmlescaped as A
B=re.compile('>\\s+<')
class Renderer(A.Factory.Renderer):
	def render_content(A,context):C=super(Renderer,A).render_content(context);return B.sub('><',C)
class C(A.Factory):Renderer=Renderer