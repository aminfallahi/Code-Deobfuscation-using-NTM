import os,sys
sys.path.insert(0,'..')
os.environ.setdefault('DJANGO_SETTINGS_MODULE','test_sqlite_zlib')
if __name__=='__main__':
	from django.core.management import execute_from_command_line as B;A=sys.argv;A.insert(1,'test')
	if len(A)==2:A.insert(2,'redis_backend_testapp');A.insert(3,'hashring_test')
	B(A)