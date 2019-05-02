from __future__ import unicode_literals
import collections as B
def A(classname='auto_namedtuple',**A):'Returns an automatic namedtuple object.\n\n    Args:\n        classname - The class name for the returned object.\n        **kwargs - Properties to give the returned object.\n    ';return B.namedtuple(classname,A.keys())(**A)