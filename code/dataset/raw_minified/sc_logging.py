'This is how logging is done inside interception script'
import logging as A
B=A.getLogger('logging-example')
if len(B.handlers)!=1:C=A.FileHandler('/var/log/jasmin/some_file.log');D=A.Formatter('%(asctime)s %(levelname)s %(message)s');C.setFormatter(D);B.addHandler(C);B.setLevel(A.DEBUG)
B.info('Got pdu: %s'%routable.pdu)