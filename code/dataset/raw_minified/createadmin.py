G=True
F='Admin'
E='admin'
import django as C
C.setup()
from django.contrib.auth import get_user_model as D
B=D()
if B.objects.count()==0:A=B.objects.create(username=E,email='admin@example.com',first_name=F,last_name=F);A.set_password(E);A.is_superuser=G;A.is_staff=G;A.save()