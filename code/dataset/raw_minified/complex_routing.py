G='index'
D='browse'
C='/'
from werkzeug.routing import Map,Rule as A,Subdomain as E,Submount as F,EndpointPrefix as B
H=Map([B('static/',[A(C,endpoint=G),A('/about',endpoint='about'),A('/help',endpoint='help')]),E('kb',[B('kb/',[A(C,endpoint=G),F('/browse',[A(C,endpoint=D),A('/<int:id>/',defaults={'page':1},endpoint=D),A('/<int:id>/<int:page>',endpoint=D)])])])])