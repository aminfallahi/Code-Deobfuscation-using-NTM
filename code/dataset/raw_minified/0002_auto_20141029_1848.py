from __future__ import unicode_literals
from django.db import models,migrations as A
from ..init import initial_settings as B,reverse_init as C
class D(A.Migration):dependencies=[('tethys_config','0001_initial')];operations=[A.RunPython(B,C)]