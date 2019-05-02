from __future__ import unicode_literals
from pipeline.conf import settings as A
from pipeline.compressors import SubProcessCompressor as B
class C(B):
	def compress_js(B,js):C=A.CLOSURE_BINARY,A.CLOSURE_ARGUMENTS;return B.execute_command(C,js)