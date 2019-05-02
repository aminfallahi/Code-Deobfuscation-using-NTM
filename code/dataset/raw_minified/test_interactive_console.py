import sys
from pyqode.core.widgets import InteractiveConsole as B
def A():
	A=B()
	if sys.platform=='win32':A.start_process('dir')
	else:A.start_process('ls')
	A.process.waitForFinished();assert A.process.exitStatus()==0