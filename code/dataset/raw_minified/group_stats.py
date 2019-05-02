from __future__ import absolute_import
from rest_framework.response import Response as C
from sentry.app import tsdb as A
from sentry.api.base import StatsMixin as B
from sentry.api.bases.group import GroupEndpoint as D
class E(D,B):
	def get(D,request,group):B=group;E=A.get_range(model=A.models.group,keys=[B.id],**D._parse_args(request))[B.id];return C(E)