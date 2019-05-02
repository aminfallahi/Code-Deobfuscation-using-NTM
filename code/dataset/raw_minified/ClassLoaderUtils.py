A=str
class B:
	'\n        Utility to get a class by name and module.\n    '
	def importClass(D,moduleName,className):B=className;C=__import__(A(moduleName),fromlist=[A(B)]);return getattr(C,A(B))