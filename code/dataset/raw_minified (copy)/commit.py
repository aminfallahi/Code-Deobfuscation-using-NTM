'!commit returns a useful commit message'
import re,requests as A
def B():return A.get('http://whatthecommit.com/index.txt').text
def C(msg,server):
	A=msg.get('text','');C=re.findall('!commit( .*)?',A)
	if not C:return
	return B()