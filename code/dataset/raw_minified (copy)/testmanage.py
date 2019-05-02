" Similar to Django's manage.py, but used only to call test with test\nsettings.\n\n"
import os,sys
if __name__=='__main__':os.environ['DJANGO_SETTINGS_MODULE']='addressbook.testsettings';from django.core.management import execute_from_command_line as A;A(sys.argv)