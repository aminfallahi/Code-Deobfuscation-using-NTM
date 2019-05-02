B=True
from whoosh import fields as A
class C(A.SchemaClass):'This describes the content that will be stored in the search index.';path=A.ID(unique=B,field_boost=2.0,stored=B);content=A.TEXT(stored=B)