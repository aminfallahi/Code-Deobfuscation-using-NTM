from __future__ import unicode_literals
from pipeline.conf import settings as A
from pipeline.compressors import SubProcessCompressor as B
class C(B):
	def compress_css(B,css):C=A.CSSMIN_BINARY,A.CSSMIN_ARGUMENTS;return B.execute_command(C,css)