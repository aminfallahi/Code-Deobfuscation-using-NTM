import djmicro as A
A.configure()
from django.shortcuts import render as B
@A.route('^$')
def C(request):return B(request,'index.html',{})
@A.route('^test/(\\d+)/$')
def D(request,id):return B(request,'test.html',{'id':id})
if __name__=='__main__':A.run()