from metakernel.tests.utils import get_kernel as C,get_log_text as D,clear_log_text,EvalKernel as E
def A():A=C(E);A.do_execute('%%javascript\n\nconsole.log("Hello from Javascript");\n');B=D(A);assert'Display Data'in B,B