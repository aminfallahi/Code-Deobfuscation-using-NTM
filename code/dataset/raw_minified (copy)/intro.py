C=getattr
A=lambda o:{A:C(o,A)for A in dir(o)if'globals'not in A and not callable(C(o,A))}
from django.db import connections as B
def D(query,params=[],db='default'):A=B[db].cursor();A.execute(query,params);return A.fetchall()