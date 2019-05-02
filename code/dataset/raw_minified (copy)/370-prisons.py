G='prison'
F='kind'
A=[(10,301,384,'Rikers Island'),(14,2621,6332,'SF County Jail')]
for (B,C,D,E) in A:assert_has_feature(B,C,D,'pois',{F:G,'name':E})
assert_has_feature(10,301,384,'landuse',{F:G})