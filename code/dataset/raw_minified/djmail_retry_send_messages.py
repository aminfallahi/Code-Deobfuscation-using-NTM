from __future__ import unicode_literals
from django.core.management.base import NoArgsCommand as B
from ...  import core as A
class C(B):
	def handle_noargs(B,**C):A._send_pending_messages();A._mark_discarded_messages();A._retry_send_messages();return 0