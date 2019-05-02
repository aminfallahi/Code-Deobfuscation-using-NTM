A=len
class B:
	def __init__(A):A.items=[]
	def __str__(B):return'Queue of size: %d'%A(B.items)
	def isEmpty(B):return A(B.items)==0
	def enqueue(A,item):A.items.insert(0,item)
	def dequeue(A):return A.items.pop()
	def size(B):return A(B.items)