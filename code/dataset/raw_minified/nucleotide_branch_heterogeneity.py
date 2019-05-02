J='root'
I='kappa'
B='nucleotide'
import pyvolve as A
C=A.read_tree(tree='((t1:0.5, t2:0.5):0.5_m1_,(t3:0.5, t4:0.5):0.5_m2_));')
D=A.Model(B,{I:3.5},name='m1')
E=A.Model(B,{I:4.75},name='m2')
F=A.Model(B,name=J)
G=A.Partition(models=[D,E,F],size=250,root_model_name=J)
H=A.Evolver(partitions=G,tree=C)
H()