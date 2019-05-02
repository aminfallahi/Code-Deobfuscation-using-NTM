D='r'
C=open
from lxml import etree as A
import StringIO as E,sys as B
F=C(B.argv[1]+'/Testing/TAG',D)
G=F.readline().strip()
H=C(B.argv[1]+'/Testing/'+G+'/Test.xml',D)
I=C(B.argv[2],D)
J=H.read()
K=I.read()
L=A.parse(E.StringIO(J))
M=A.XML(K)
N=A.XSLT(M)
O=N(L)
print(O)