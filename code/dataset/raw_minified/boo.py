import os
class A(Package):
	def __init__(A):Package.__init__(A,'boo','0.9.4.9',sources=['http://dist.codehaus.org/boo/distributions/boo-0.9.4.9.tar.gz'])
	def install(A):
		for B in ['booc','booi','booish']:replace_in_file(os.path.join('extras',B),{'${exec_prefix}':A.package_prefix})
		A.sh('make install MIME_PREFIX=/tmp GTKSOURCEVIEW_PREFIX=/tmp DESTDIR=%{stage_root}')
A()