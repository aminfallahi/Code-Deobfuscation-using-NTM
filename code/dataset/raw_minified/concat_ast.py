import itertools as A
from ..language.ast import Document as B
def C(asts):return B(definitions=list(A.chain.from_iterable((A.definitions for A in asts))))