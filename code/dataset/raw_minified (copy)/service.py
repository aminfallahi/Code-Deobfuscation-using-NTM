C='Input protocol factory'
from zope.interface import Interface as B,Attribute as A
class D(B):iprot_factory=A(C);oprot_factory=A(C);processor=A('Thrift processor')