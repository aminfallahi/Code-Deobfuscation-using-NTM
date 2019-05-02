' tokenize data to match existing dataset '
from __future__ import absolute_import,division,print_function
import fileinput as C,re as B
D='trec_2002_final.txt'
for A in C.input(D):A=B.sub('([.!?])$',' \\1',A);A=B.sub('(\\w+)([.!?])','\\1 \\2',A);A=B.sub("'(.*)'","` \\1 '",A);A=B.sub('"(.*)"',"`` \\1 ''",A);A=B.sub("(\\w+)'s","\\1 's",A);A=B.sub("(\\w+)'","\\1 '",A);A=B.sub('(\\w+)([,:;-]) ','\\1 \\2 ',A);print(A.strip())