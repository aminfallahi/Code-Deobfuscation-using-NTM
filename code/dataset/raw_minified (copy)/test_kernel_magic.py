from metakernel.tests.utils import get_kernel as C,get_log_text as D,EvalKernel as E
import os,time
def A():A=C(E);A.do_execute('%kx 42',False);B=D(A);assert'42'in B,B