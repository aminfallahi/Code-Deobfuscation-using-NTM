import sys,os as A
sys.path.append(A.path.abspath(A.path.join(A.path.dirname(__file__),A.pardir)))
sys.path.append(A.path.abspath(A.path.join(A.path.dirname(__file__),A.pardir,A.pardir)))
__import__('manage')
A.environ['DJANGO_SETTINGS_MODULE']='settings'