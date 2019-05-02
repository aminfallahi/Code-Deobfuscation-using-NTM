import os
from __main__ import slicer
from .  import SlicerUtil as C
class A:
	def __init__(A,moduleName):B=moduleName;A.__moduleName__=B;A.__settingsPath__=os.path.join(C.getModuleFolder(B),'Resources',B+'_storage.csv');print(A.__settingsPath__)