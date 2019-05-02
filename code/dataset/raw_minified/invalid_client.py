from .base import InvalidClient as A
class B(A):reason='The client was malformed or invalid.'
class C(A):reason='The client secret was malformed or invalid.'