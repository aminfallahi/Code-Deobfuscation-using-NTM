from gluon.html import URL
from gluon.http import redirect as A
from s3 import S3CustomController as B
class C(B):
	' Custom Home Page '
	def __call__(B):A(URL(c='project',f='activity',args=['summary']))