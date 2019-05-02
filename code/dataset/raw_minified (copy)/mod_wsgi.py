from __future__ import absolute_import
from django.http import HttpResponse as C
from ._internalredirect import _convert_file_to_url as D
def A(request,filename,**E):A=request;B=C();B['Location']=D(filename);A.get_host=lambda:'';A.build_absolute_uri=lambda location:location;return B