import pyvolve as A
B=A.read_tree(file='file_with_tree.tre')
C=A.Model('nucleotide')
D=A.Partition(models=C,size=250)
E=A.Evolver(partitions=D,tree=B)
E()