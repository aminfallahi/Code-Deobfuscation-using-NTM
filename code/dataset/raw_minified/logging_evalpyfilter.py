import logging as B
A=B.getLogger('jasmin-router')
A.debug('Inside evalpy-test.py')
if routable.user.username=='Evalpyusr2':A.info("Routable's username is Evalpyusr2 !");C=False
else:A.info("Routable's username is not Evalpyusr2: %s"%routable.user.username);C=True