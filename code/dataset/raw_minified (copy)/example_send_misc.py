E='http://127.0.0.1:1401/send?%s'
D='content'
import urllib2 as B,urllib as C
A={'username':'foo','password':'bar','to':'+336222172',D:'Hello'}
A[D]='Very long message ....................................................................................................................................................................................'
B.urlopen(E%C.urlencode(A)).read()
A[D]='\x06#\x061\x06F\x06('
A['coding']=8
B.urlopen(E%C.urlencode(A)).read()