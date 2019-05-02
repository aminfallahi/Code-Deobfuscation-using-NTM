from .  import importer as A
A.install(check_options=True)
from django.core.management import execute_from_command_line,call_command