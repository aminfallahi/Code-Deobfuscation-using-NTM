G=set
F=len
from django.core.management.base import BaseCommand as A
from account.models import UserProfile as E
from submission.models import Submission as C
class B(A):
	def handle(B,*L,**M):
		K='problem_id';D=True;B.stdout.write(B.style.SUCCESS('Please wait a minute'))
		for A in E.objects.all():H=C.objects.filter(user_id=A.user.id);A.submission_number=H.count();I=F(G(C.objects.filter(user_id=A.user.id,contest_id__isnull=D).values_list(K,flat=D)));J=F(G(C.objects.filter(user_id=A.user.id,contest_id__isnull=False).values_list(K,flat=D)));A.accepted_problem_number=I+J;A.save()
		B.stdout.write(B.style.SUCCESS('Succeeded'))