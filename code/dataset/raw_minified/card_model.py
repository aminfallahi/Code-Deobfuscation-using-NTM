D=True
from django.db import models as A
from django.core.urlresolvers import reverse as C
from markitup.fields import MarkupField as B
from cardbox.deck_model import Deck
class E(A.Model):
	ID=A.AutoField(primary_key=D);deck=A.ForeignKey(Deck);front=B();back=B();created=A.DateTimeField(auto_now_add=D)
	def __unicode__(A):return A.front.raw
	def get_absolute_url(A):'Returns the unique url to this object';return C('card:card_detail',kwargs={'pk':A.ID})