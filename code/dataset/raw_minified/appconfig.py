import django as B
def A():from flows import statestore as A;A.setup()
if B.VERSION>=(1,7):
	from django.apps import AppConfig as C
	class D(C):
		name='flows'
		def ready(B):A()
else:A()