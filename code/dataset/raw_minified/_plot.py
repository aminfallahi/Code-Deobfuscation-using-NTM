__author__='olga'
from prettyplotlib.utils import remove_chartjunk as D,maybe_get_ax as E
from prettyplotlib.colors import pretty as A
@A
def B(*B,**A):C,B,A=E(*B,**A);F=A.pop('show_ticks',False);G=C.plot(*B,**A);D(C,['top','right'],show_ticks=F);return G