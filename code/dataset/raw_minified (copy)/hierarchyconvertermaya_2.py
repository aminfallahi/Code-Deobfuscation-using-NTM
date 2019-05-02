'Window is parented properly.'
D=None
import hierarchyconvertergui as B,mayautils as C
A=D
def E():
	global A
	if A is D:E=B.HierarchyConverterController();F=C.get_maya_window();A=B.create_window(E,F)
	A.show()