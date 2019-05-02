H='header'
from zerotest.utils.io_helper import StringIO as A
from zerotest.record.formatter import Formatter as E
from zerotest.request import Request as F
from zerotest.response import Response as G
B=F(scheme='http',method='get',params='query_string=here',host='example.com',path='/test',headers={'just':H},data='request')
C=G(status=200,headers={'responsed':H},body='response')
D=E()
def I():E=A();D.write_record(E,B,C);F=A(E.getvalue());G,H=D.read_record(F);assert B.__dict__==G.__dict__;assert C.__dict__==H.__dict__