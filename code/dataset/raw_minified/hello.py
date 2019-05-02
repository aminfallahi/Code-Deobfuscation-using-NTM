from importd import d
@d('/')
def A(request):return d.HttpResponse('hello world')
if __name__=='__main__':d.main()