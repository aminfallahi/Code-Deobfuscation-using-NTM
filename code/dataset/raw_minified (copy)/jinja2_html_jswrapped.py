from __future__ import absolute_import,division,print_function,unicode_literals
from ..utils import to_javascript as B
from .  import jinja2_htmlescaped as A
class Renderer(A.Factory.Renderer):
	def render_content(A,context):C=super(Renderer,A).render_content(context);return'document.write(%s)'%B(C)
class C(A.Factory):Renderer=Renderer