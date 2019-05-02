from .base import UnsupportedGrantType as A
class B(A):reason='The grant type was malformed or invalid.'
class C(A):reason='The provided grant type is not supported.'