A='..'
import os,sys
sys.path.insert(0,os.path.join(os.path.dirname(__file__),A,A))
from importd import d
d(DEBUG=True,INSTALLED_APPS=['app'],autoimport=False,SETTINGS_MODULE='main')
if __name__=='__main__':d.main()