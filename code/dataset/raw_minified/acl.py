from mongoengine import EmbeddedDocument as A
class B(A):meta=dict(allow_inheritance=True)