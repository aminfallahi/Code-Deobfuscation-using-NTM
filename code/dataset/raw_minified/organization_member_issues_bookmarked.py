from __future__ import absolute_import
from sentry.api.bases import OrganizationIssuesEndpoint as A
from sentry.models import Group
class B(A):
	def get_queryset(A,request,organization,member,project_list):return Group.objects.filter(bookmark_set__user=member.user,bookmark_set__project__in=project_list).extra(select={'sort_by':'sentry_groupbookmark.date_added'}).order_by('-sort_by')