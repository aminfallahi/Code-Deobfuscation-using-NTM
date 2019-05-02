G='form-control'
F='class'
E='description'
D='title'
from django.forms import ModelForm as A
from django.forms.widgets import Textarea as B,TextInput as C
from deck_model import Deck
class H(A):
	'The basic form for updating or editing decks'
	class Meta:model=Deck;fields=D,E;widgets={D:C(attrs={F:G}),E:B(attrs={F:G})}