from google.appengine.api import images as B
from django import forms
from app.models.upload import UploadModel as A
class C(forms.ModelForm):
	class Meta:model=A
	def clean_file(C):A=C.cleaned_data['file'];return{'img':B.resize(A.read(),320,320),'content_type':A.content_type}