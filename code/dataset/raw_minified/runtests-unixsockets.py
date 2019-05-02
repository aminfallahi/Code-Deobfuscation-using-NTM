import os,sys
os.environ.setdefault('DJANGO_SETTINGS_MODULE','test_sqlite_usock')
sys.path.insert(0,'tests')
if __name__=='__main__':from django.core.management import execute_from_command_line as B;A=sys.argv;A.insert(1,'test');B(A)