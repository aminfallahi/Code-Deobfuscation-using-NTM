'\nRuns a Django management command, using the vendor library.\n\n'
import os,sys
from moztrap.deploy.paths import add_vendor_lib as A
if __name__=='__main__':A();os.environ.setdefault('DJANGO_SETTINGS_MODULE','moztrap.settings.default');from django.core.management import execute_from_command_line as B;B(sys.argv)