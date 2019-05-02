from metakernel.tests.utils import get_kernel as B,get_log_text as C
def A():A=B();A.do_execute('%magic',None);D=C(A);assert'! COMMAND ... - execute command in shell'in D