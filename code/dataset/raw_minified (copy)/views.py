from django.shortcuts import render as A
from testproj.testapp import models as B
def C(request):return A(request,'test_index.html',{'secret_files':B.SecretFile.objects.all()})