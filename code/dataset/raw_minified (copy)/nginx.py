from django import http
def A(request,thumbnail,**B):A=http.HttpResponse();A['X-Accel-Redirect']=thumbnail.url;del A['Content-Type'];return A