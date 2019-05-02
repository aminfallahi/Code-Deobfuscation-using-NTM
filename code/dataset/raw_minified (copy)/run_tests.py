import os,sys,django as B
if __name__=='__main__':
	os.environ.setdefault('DJANGO_SETTINGS_MODULE','tests.settings');B.setup();from django.test.runner import DiscoverRunner as C;D=C(verbosity=2);A=D.run_tests(['tests.base'])
	if A:sys.exit(A)