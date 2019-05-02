I=zip
H=tuple
from datetime import datetime as F
import pytz as A
J=H(I(A.all_timezones,A.all_timezones))
K=H(I(A.common_timezones,A.common_timezones))
B=[]
for C in A.common_timezones:G=F.now(A.timezone(C));D=G.strftime('%z');B.append((int(D),C,'(GMT%s) %s'%(D,C)))
B.sort()
for E in xrange(len(B)):B[E]=B[E][1:]