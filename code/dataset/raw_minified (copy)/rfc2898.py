from pyasn1.type import univ as A,namedtype as B
class C(A.Sequence):componentType=B.NamedTypes(B.NamedType('salt',A.OctetString()),B.NamedType('iterationCount',A.Integer()))