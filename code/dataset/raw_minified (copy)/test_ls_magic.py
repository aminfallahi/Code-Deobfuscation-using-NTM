import os
from metakernel.tests.utils import get_kernel as E,get_log_text as C,clear_log_text as D
def A():A=E();A.do_execute('%ls /tmp');B=C(A);assert'/tmp/'in B,B[:100];D(A);A.do_execute('%ls /tmp --recursive');B=C(A);assert'/tmp'in B,B[:100];D(A)