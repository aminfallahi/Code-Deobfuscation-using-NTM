C='Heroku Platform API'
B='title'
from valor.schema import Schema as A
from .fixtures import schema_fname
def D(schema_fname):D=A.from_file(schema_fname);assert D[B]==C
def E(schema_fname):
	with open(schema_fname)as D:E=A.from_file(D);assert E[B]==C
def F(schema_fname):C='app';B=A.from_file(schema_fname);assert B.resolve_ref(B['properties'][C]['$ref'])==B['definitions'][C]