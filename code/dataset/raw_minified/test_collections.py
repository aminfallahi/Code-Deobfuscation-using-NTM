from vispy.visuals.collections import PathCollection as A,PointCollection as B,PolygonCollection as C,SegmentCollection as D,TriangleCollection as E
from vispy.testing import requires_application as F,TestingCanvas as G
@F()
def H():
	'Test collection initialization\n    '
	with G():
		for F in (A,B,C,D,E):F()