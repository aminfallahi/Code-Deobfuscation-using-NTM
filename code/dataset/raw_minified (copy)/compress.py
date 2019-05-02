' Filter to remove whitespace from input CSS '
from __future__ import absolute_import
import re
from pipeline.compressors import CompressorBase as A
class B(A):
	_COMMENT_RE=re.compile('/\\*.*?\\*/');_WHITESPACE_RE=re.compile('[ \\t\\n\\r]+')
	def compress_css(B,css):A=css;A=B._COMMENT_RE.sub('',A);A=B._WHITESPACE_RE.sub(' ',A);return A.strip()