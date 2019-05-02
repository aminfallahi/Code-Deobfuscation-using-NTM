_A='NAME'
from pytest_django_test.settings_base import *
db_name='DBNAME_pytest_django_db'+db_suffix
test_db_name='test_'+db_name+'_db_test'
DATABASES={'default':{'ENGINE':'django.db.backends.sqlite3',_A:db_name,'TEST':{_A:test_db_name},'TEST_NAME':test_db_name}}