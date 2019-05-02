import platform as B,uuid as A
print(A.uuid5(A.NAMESPACE_DNS,B.node()+str(A.getnode())).hex)