import matplotlib.pyplot as D,prettyplotlib as A,numpy as B
C=D.figure()
E=C.add_subplot(111)
B.random.seed(123)
F=B.random.normal(loc=1,size=(6,6),scale=0.2)
G=B.random.normal(size=(6,6),scale=0.2)
A.beeswarm([F,G],colors=[A.colors.set1[1],A.colors.set1[2]],xticklabels=['data1','data2'])
E.set_ylabel('Mean')
C.savefig('plot.png')