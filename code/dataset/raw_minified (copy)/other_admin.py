from django.contrib.admin.sites import AdminSite as A
from simple_history.admin import SimpleHistoryAdmin as B
from .models import State
C=A(name='other_admin')
C.register(State,B)