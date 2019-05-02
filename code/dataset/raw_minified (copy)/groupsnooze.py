from __future__ import absolute_import
from django.db import models as A
from sentry.db.models import Model,FlexibleForeignKey as B,sane_repr as C
class D(Model):
	__core__=False;group=B('sentry.Group',unique=True);until=A.DateTimeField()
	class Meta:db_table='sentry_groupsnooze';app_label='sentry'
	__repr__=C('group_id')