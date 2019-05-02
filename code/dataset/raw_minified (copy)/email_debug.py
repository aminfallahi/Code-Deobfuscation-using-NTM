import smtpd,asyncore as A
B=smtpd.DebuggingServer(('127.0.0.1',1025),None)
A.loop()