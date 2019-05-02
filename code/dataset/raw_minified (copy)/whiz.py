'Dummy shovel tasks for testing'
from __future__ import print_function
B=print
from shovel import task as A
@A
def C():'Dummy function';B('Hello from bar!')
@A
def D():'Dummy function';B('Hello from foo!')