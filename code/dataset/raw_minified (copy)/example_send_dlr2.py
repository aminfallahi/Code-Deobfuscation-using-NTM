import urllib2 as A,urllib as B
C={'username':'foo','password':'bar','to':'+336222172','content':'Hello','dlr-url':'http://myserver/acknowledgement','dlr-level':2}
A.urlopen('http://127.0.0.1:1401/send?%s'%B.urlencode(C)).read()