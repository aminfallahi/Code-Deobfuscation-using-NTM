from thrift.Thrift import TType,TMessageType,TException,TApplicationException
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol,TProtocol
try:from thrift.protocol import fastbinary as A
except:A=None