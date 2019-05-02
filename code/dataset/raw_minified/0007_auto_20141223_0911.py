from __future__ import unicode_literals
B='crash'
from django.db import models,migrations as A
class C(A.Migration):dependencies=[(B,'0006_crash_signature')];operations=[A.RenameField(model_name=B,old_name='mini_dump',new_name='upload_file_minidump')]