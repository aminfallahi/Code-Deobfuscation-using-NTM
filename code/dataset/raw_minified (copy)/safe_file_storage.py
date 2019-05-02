from django.core.files.storage import FileSystemStorage as A
from django.template.defaultfilters import slugify as C
import os
class D(A):
	def get_valid_name(E,name):"\n        Returns a filename, based on the provided filename, that's suitable for\n        use in the target storage system. (slugify)\n        ";F=super(D,E).get_valid_name(name);A,B=os.path.splitext(F);A=C(A);B=C(B);return'%s.%s'%(A,B)