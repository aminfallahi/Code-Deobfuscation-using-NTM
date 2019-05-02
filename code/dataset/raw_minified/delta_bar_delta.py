from neupy.core.properties import ProperFractionProperty as A,BoundedProperty as B
from .base import SingleStepConfigurable as C
__all__='DeltaBarDelta',
class D(C):beta=A(default=0.5);increase_factor=B(default=0.1,minval=0);decrease_factor=A(default=0.9)