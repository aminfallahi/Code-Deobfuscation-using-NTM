'Piggyback on pyserial terminal'
from serial.tools import miniterm as A
import sys
from .utils import default_port as B
def C(port=B(),baud='9600'):'Launch minterm from pyserial';B=['nodemcu-uploader',port,baud];sys.argv=B;A.main()