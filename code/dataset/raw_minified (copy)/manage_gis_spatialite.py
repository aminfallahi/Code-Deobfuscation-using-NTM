import os,sys
if __name__=='__main__':os.environ.setdefault('DJANGO_SETTINGS_MODULE','settings_gis_spatialite');from django.core.management import execute_from_command_line as A;A(sys.argv)