G=None
import os
from django.template.loaders.filesystem import Loader as A
from accounts.models import get_template as E
import settings as B
class F(A):
	def get_template_sources(H,template_name,template_dirs=G):
		A=template_dirs
		if not A:
			C=B.DEFAULT_TEMPLATE;D=getattr(B,'request_handler',G);A=B.TEMPLATE_DIRS
			if D:C=E(D)
			A=[os.path.join(B,C)for B in A];A=tuple(A)
		return super(F,H).get_template_sources(template_name,A)