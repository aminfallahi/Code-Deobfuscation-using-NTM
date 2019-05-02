from base import Base
class A(Base):
	def pop(A):return A._loads(A.redis.lpop(A.name))
	def push(A,item):
		assert item
		try:A.redis.lpush(A.name,A._dumps(item));return True
		except:return False