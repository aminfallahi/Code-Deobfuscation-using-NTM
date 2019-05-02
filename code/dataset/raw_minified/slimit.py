from __future__ import absolute_import,unicode_literals
from pipeline.compressors import CompressorBase as A
class B(A):
	'\n    JS compressor based on the Python library slimit\n    (http://pypi.python.org/pypi/slimit/).\n    '
	def compress_js(B,js):from slimit import minify as A;return A(js)