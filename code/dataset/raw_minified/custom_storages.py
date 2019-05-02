from django.conf import settings as A
from storages.backends.s3boto import S3BotoStorage as B
class C(B):location=A.STATICFILES_LOCATION;bucket_name=''
class D(B):location=A.MEDIAFILES_LOCATION;bucket_name=''