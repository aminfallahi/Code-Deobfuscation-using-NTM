from osgeo import ogr
E=ogr.Open('D:\\osgeopy-data\\Galapagos')
B=E.GetLayerByName('albatross_ranges2')
B.SetAttributeFilter("tag_id = '1163-1163' and location = 'island'")
A=next(B)
C=A.geometry().Clone()
D=A.geometry().Clone()
for A in B:C=C.Union(A.geometry());D=D.Intersection(A.geometry())
F=D.GetArea()/C.GetArea()*100
print('Percent of all area used in every visit: {0}'.format(F))