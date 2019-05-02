import os
from metakernel.tests.utils import get_kernel as B,get_log_text as C,clear_log_text as D
def A():A=B();A.do_execute('%cd ~');assert os.getcwd()==os.path.expanduser('~'),os.getcwd();D(A);A.do_execute('%cd');assert os.getcwd()in C(A)