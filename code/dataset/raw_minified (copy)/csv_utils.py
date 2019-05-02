B=''
A=None
from datetime import datetime as D
class C:
	def coalesce_date(C):return B if C is A else D.strftime(C,'%Y-%m-%d %H:%M:%S')
	def coalesce_bool(C):return B if C is A else'true'if C is True else'false'
	def coalesce_int(C):return B if C is A else str(C)