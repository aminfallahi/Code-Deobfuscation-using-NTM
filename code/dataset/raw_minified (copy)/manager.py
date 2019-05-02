from __future__ import absolute_import
__all__=['VcsManager']
class VcsManager:
	def __init__(A):A.backends={}
	def add(A,name,cls):A.backends[name]=cls
	def get(A,name,**B):return A.backends.get(name)(**B)