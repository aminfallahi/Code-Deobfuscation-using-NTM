from .base import MessageBase as A
from django.utils.translation import ugettext as B
class C(A):
	'Simple plain text message class to allow schedule_messages()\n    to accept message as a simple string instead of a message object.\n\n    ';alias='plain';title=B('Text notification')
	def __init__(A,text):super(C,A).__init__({A.SIMPLE_TEXT_ID:text})