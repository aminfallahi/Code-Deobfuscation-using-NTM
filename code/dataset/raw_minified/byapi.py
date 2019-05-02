from circus import get_arbiter as B
C={'cmd':'python','args':'-u dummy_fly.py $(circus.wid)','numprocesses':3}
A=B([C],debug=True)
try:A.start()
finally:A.stop()