class A:
	def __init__(A,commit_hash,date,author):A.commit_hash=commit_hash;A.date=date;A.author=author
	def __str__(A):return'%s %s %s'%(A.commit_hash,A.date,A.author)
	def __eq__(A,other):B=other;return A.commit_hash==B.commit_hash and A.date==B.date and A.author==B.author