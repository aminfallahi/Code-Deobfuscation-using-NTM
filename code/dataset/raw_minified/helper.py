import calendar as A
from datetime import datetime as B
def C(ts):return B.utcfromtimestamp(float(ts))
def D(dt):return A.timegm(dt.timetuple())