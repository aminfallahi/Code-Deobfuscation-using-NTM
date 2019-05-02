B=False
import sys as A
if A.platform.startswith('linux'):from attic.platform_linux import acl_get,acl_set,API_VERSION
elif A.platform.startswith('freebsd'):from attic.platform_freebsd import acl_get,acl_set,API_VERSION
elif A.platform=='darwin':from attic.platform_darwin import acl_get,acl_set,API_VERSION
else:
	API_VERSION=2
	def acl_get(path,item,st,numeric_owner=B):0
	def acl_set(path,item,numeric_owner=B):0