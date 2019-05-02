import json
from django import template as A
from django.forms.models import model_to_dict as B
from calaccess_campaign_browser.utils.lazyencoder import LazyEncoder as C
D=A.Library()
@D.filter
def E(obj):'\n    Renders a Django model object as a JSON object.\n    ';A=B(obj);return json.dumps(A,cls=C)