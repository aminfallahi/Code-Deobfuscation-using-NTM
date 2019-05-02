from django.core.management.base import NoArgsCommand as A
from events.models import Calendar as B
class C(A):
	'\n    Imports ICS calendars.\n    When used in cron jobs, it is advised to add file-locking by using the flock(1)\n    command. Eg::\n\n        flock -n import_ics_calendars.lock -c django-admin.py import_ics_calendars --settings=pydotorg.settings.local\n\n    '
	def handle_noargs(D,*E,**F):
		A=B.objects.filter(url__isnull=False)
		for C in A:C.import_events()