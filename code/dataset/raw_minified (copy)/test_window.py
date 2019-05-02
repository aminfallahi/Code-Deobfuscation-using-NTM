B=next
from textplot.utils import window as C
def A():'\n    window() should generate a sliding window over an iterable.\n    ';D=[1,2,3,4,5,6];A=C(D,3);assert B(A)==(1,2,3);assert B(A)==(2,3,4);assert B(A)==(3,4,5);assert B(A)==(4,5,6)