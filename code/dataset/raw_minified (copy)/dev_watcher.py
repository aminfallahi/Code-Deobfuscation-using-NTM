from sparts.tasks.file import DirectoryWatcherTask as A
from sparts.vservice import VService as B
class C(A):INTERVAL=1.0;PATH='/dev'
C.register()
if __name__=='__main__':B.initFromCLI()