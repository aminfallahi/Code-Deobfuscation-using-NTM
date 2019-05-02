from django import template as A
from ..models import CodeSample as B
C=A.Library()
@C.assignment_tag
def D(limit=5):' Return last 5 published code samples ';return B.objects.published()[:limit]