from django import template as A
from announcement.models import Announcement as B
def C():return B.objects.filter(visible=True).order_by('-create_time')
D=A.Library()
D.assignment_tag(C,name='public_announcement_list')