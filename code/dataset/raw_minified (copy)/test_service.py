from valor.service import Service as A
from valor.resource import Resource as B
from .fixtures import schema,session
def C(schema,session):C=A(schema,session);assert type(C.app)==B
def D(schema,session):B=A(schema,session);assert dir(B)[0:3]==['account','account_feature','addon']