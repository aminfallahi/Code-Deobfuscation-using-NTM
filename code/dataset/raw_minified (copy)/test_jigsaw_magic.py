E='workspace1.html'
from metakernel.tests.utils import get_kernel as B,get_log_text as C,clear_log_text,EvalKernel as D
import os
def A():A=B(D);A.do_execute('%jigsaw Processing --workspace workspace1');F=C(A);assert os.path.isfile(E),'File does not exist: workspace1.html'
def F():
	for A in [E]:
		try:os.remove(A)
		except:pass