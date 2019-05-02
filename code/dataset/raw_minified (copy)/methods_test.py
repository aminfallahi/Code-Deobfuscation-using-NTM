from feather import http
def A(req,res):res.respond('Hello World!')
def B(req,res):res.respond_json(req.get('form'))
C={'/':A,'/post_test':{'POST':B}}
http.start(C)