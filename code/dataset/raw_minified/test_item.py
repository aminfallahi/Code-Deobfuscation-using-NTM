from bepasty.storage.filesystem import Item
def A(tmpdir):
	F=None;E='w+b';A=tmpdir;C=A.join('test.meta');D=A.join('test.data')
	with Item(C.open(E),D.open(E))as B:assert B.data is not F;assert B.meta is not F