D='train'
C='service'
B='kind'
A='transit'
assert_has_feature(5,5,12,A,{B:D,C:'long_distance'})
assert_has_feature(5,9,12,A,{B:D,C:'high_speed'})
assert_has_feature(5,9,12,A,{B:D,C:'international'})