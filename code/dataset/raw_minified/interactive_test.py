E='okcupyd'
D='argv'
import sys as C,mock as A,okcupyd as B
@A.patch.object(C,D,[E])
@A.patch.object(C,'exit')
@A.patch.object(B.IPython,'embed')
@A.patch.object(B,'User')
def F(*F):
	B.interactive()
	with A.patch.object(C,D,[E,'-v']):B.interactive()