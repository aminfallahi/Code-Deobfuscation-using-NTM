from __future__ import print_function,division,absolute_import
from numba.targets.descriptors import TargetDescriptor as A
from numba.targets.options import TargetOptions as B
from .target import HSATargetContext as C,HSATypingContext as D
class E(B):OPTIONS={}
class F(A):options=E;typingctx=D();targetctx=C(typingctx)