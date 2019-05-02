from __future__ import absolute_import
from picklefield.fields import PickledObjectField as A
class B(A):
	def get_db_prep_value(C,value,*D,**E):
		A=value
		if isinstance(A,str):A=A.decode('utf-8')
		return super(B,C).get_db_prep_value(A,*D,**E)