F='image_tag'
from django.contrib import admin as A
from models import FileModel as B,BasicFilesModel as C
class D(A.ModelAdmin):0
class E(A.ModelAdmin):readonly_fields=F,;list_display='__unicode__',F
A.site.register(B,E)
A.site.register(C,D)