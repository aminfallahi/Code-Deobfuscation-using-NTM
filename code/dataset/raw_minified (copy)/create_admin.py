D=True
C='ADMIN_PASSWORD'
B='ADMIN_USER'
import os
if B in os.environ and C in os.environ:from django.contrib.auth.models import User;A=User.objects.create_user(os.environ[B],password=os.environ[C]);A.is_superuser=D;A.is_staff=D;A.save()