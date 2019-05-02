from feather import http
def A(req,res):res.respond('Hello {}!'.format(req['params']['name']))
def B(req,res):res.respond('Hello World!')
http.start({'/<name>':A,'/':B})