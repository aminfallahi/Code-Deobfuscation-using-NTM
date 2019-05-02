F=len
def A(test,expected,actual):
	G='\n';A=1;B=expected.split(G);C=actual.split(G)
	for (D,E) in zip(B,C):test.assertEquals(E,D,"%s: '%s' != '%s'"%(A,E,D));A+=1
	test.assertEquals(F(B),F(C))