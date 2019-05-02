'\nSetup Django environment for tests or for Python shell.\n'
import os,sys
def A():
	os.environ['DJANGO_SETTINGS_MODULE']='mail_templated.test_utils.settings';B=os.path.dirname(os.path.dirname(os.path.dirname(__file__)));sys.path.insert(0,B);import django as A
	if hasattr(A,'setup'):A.setup()