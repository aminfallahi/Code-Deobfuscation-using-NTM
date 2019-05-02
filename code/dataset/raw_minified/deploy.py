from django.core.management.base import BaseCommand as A,CommandError
from underwear.run_underwear import deploy as B
class C(A):
	args='[hosts file location] [private key path and filename] [custom'+' app variables]';help='Deploy to one or more remote servers.'
	def handle(K,*A,**L):
		J='@%s';I='--extra-vars';H='--private-key=%s';G='deployer';F='-u';E='-K';D='-i';C='django-stack.yml'
		if len(A)<3:B([C,D,'./deploy/hosts',E,F,G,H%'./deploy/ssh_conf/id_rsa',I,J%'./deploy/underwear.yml'])
		else:B([C,D,A[0],E,F,G,H%A[1],I,J%A[2]])