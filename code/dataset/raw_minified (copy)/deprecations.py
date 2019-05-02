from __future__ import unicode_literals
import warnings as A
class B(DeprecationWarning):''
def C(message):A.warn(message,B)
A.simplefilter('default',B)