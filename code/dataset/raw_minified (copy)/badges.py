from django.conf import settings as A
from django.dispatch import receiver as B
from badger.signals import badge_was_awarded as C
from kitsune.kbadge.tasks import send_award_notification as D
@B(C)
def E(sender,award,**B):
	'Notifies award recipient that he/she has an award!'
	if not A.STAGE:D.delay(award)