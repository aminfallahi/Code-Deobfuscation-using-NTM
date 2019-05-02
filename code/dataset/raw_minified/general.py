E='__doc__'
import matplotlib.pyplot as A
from functools import partial as B,update_wrapper as C
from prettyplotlib.colors import pretty as D
@B(C,wrapped=A.subplots,assigned=[E])
@D
def F(*B,**C):return A.subplots(*B,**C)
@B(C,wrapped=A.subplot2grid,assigned=[E])
@D
def G(*B,**C):return A.subplot2grid(*B,**C)