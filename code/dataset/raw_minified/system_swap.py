import psutil as C
from checks import AgentCheck as A
class B(A):
	def check(A,instance):B=C.swap_memory();A.rate('system.swap.swapped_in',B.sin);A.rate('system.swap.swapped_out',B.sout)