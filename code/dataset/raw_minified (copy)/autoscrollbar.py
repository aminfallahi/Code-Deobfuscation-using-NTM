B=float
import ttk
class A(ttk.Scrollbar):
	def set(A,lo,hi):
		if B(lo)<=0.0 and B(hi)>=1.0:A.tk.call('grid','remove',A)
		else:A.grid()
		ttk.Scrollbar.set(A,lo,hi)