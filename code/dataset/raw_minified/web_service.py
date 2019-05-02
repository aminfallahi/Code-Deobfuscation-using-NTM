_C='not specified'
_B='foo'
_A="'foo' is: %s"
from itty import *
@get('/get/(?P<name>\\w+)')
def test_get(request,name=', world'):return'Hello %s!'%name
@post('/post')
def test_post(request):return _A%request.POST.get(_B,_C)
@put('/put')
def test_put(request):return _A%request.PUT.get(_B,_C)
@delete('/delete')
def test_delete(request):return'Method received was %s.'%request.method
run_itty()