from valor.resource import Resource as A
from .fixtures import schema,session
def B(schema,session):B=A(schema,session,'config-var');assert dir(B)==['info','update']