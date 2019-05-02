from __future__ import absolute_import
import funcfinder.questions.math as A
from funcfinder.utils import solves as B
@B(A.is_divisible_by)
def C(a,b):return a%b==0
@B(A.is_even)
def D(a):return C(a,2)