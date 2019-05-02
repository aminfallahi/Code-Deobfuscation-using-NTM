import sys as A,os.path
C=os.path.abspath(A.path[0])
A.path=[B for B in A.path if os.path.abspath(B)!=C]
from epydoc.cli import cli
cli()