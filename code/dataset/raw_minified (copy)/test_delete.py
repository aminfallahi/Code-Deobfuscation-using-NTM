from django.core.urlresolvers import reverse as B
from django.utils.encoding import force_bytes as C
from tests import models as D
import pytest as A
E=A.mark.django_db
def F(client):E=D.Person.objects.create(name='test');A=client.delete(B('person-detail',args=[E.id]));assert A.status_code==204;assert A.content==C('')