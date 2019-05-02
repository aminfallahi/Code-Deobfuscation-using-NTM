import logging as B
from marrow.mailer import Message as C,Mailer as D
B.basicConfig(level=B.INFO)
A=D({'manager.use':'immediate','transport.use':'maildir','transport.directory':'data/maildir'})
A.start()
E=C([('Alice Bevan-McGregor','alice@gothcandy.com')],[('Alice Two','alice.mcgregor@me.com')],'This is a test message.',plain='Testing!')
A.send(E)
A.stop()