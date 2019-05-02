import pstats as D,sys as A
if len(A.argv)>=2 and A.argv[1].count('.dat'):B=A.argv[1]
else:B='profile.dat'
C=D.Stats(B)
if'highest'in A.argv:C.sort_stats('cumulative').print_stats(20)
else:C.strip_dirs().sort_stats(-1).print_stats()