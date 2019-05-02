from __future__ import print_function
from webassets.filter import Filter as A
from webassets.exceptions import FilterError
from react import jsx
class B(A):
	name='jsx';max_debug_level=None
	def output(A,_in,out,**B):out.write(jsx.transform_string(_in.read().encode('utf-8')))