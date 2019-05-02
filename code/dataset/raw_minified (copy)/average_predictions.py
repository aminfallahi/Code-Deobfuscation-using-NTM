import numpy as B,sys as A
if len(A.argv)<3:A.exit('Usage: python average_predictions.py <predictions_file1> [predictions_file_2] [...] <output_file>')
C=A.argv[1:-1]
D=A.argv[-1]
E=[B.load(A)for A in C]
F=B.mean(E,axis=0)
B.save(D,F)