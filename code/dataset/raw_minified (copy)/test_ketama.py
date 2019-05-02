from rc.ketama import HashRing as B
def A():
	A=['node01','node02','node03','node04'];C=B(A);D=['key-%s'%A for A in range(1000)];E=[C.get_node(A)for A in D]
	for F in A:assert F in E