from vispy.util.dpi import get_dpi as B
from vispy.testing import run_tests_if_main as A
def C():'Test dpi support';A=B();assert A>0.0;assert isinstance(A,float)
A()