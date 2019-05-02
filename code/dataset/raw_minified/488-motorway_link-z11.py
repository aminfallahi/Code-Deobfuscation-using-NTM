J='motorway_link'
I='yes'
H='is_link'
G='kind'
F='roads'
A='highway'
E=[(11,327,791),(11,603,769)]
for (B,C,D) in E:assert_has_feature(B,C,D,F,{G:A,H:I,A:J});assert_no_matching_feature(B-1,C/2,D/2,F,{G:A,H:I,A:J})