C=False
B=getattr
from django.conf import settings as A
D=B(A,'DBLOG_CATCH_404_ERRORS',C)
E=B(A,'DBLOG_ENHANCED_TRACEBACKS',True)
F=B(A,'DBLOG_DATABASE_USING',None)
G=B(A,'DBLOG_USE_LOGGING',C)
H=B(A,'DBLOG_THRASHING_TIMEOUT',60)
I=B(A,'DBLOG_THRASHING_LIMIT',10)