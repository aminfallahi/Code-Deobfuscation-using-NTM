from ....fields import DecimalField as A
from .widgets import USDecimalInput as B
from decimal import Decimal as C
class D(A):
	widget=B
	def to_python(A,value):return C(value)