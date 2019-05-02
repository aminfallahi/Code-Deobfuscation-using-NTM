class A(Package):
	def __init__(A):Package.__init__(A,'libxml2','2.9.1',configure_flags=['--with-python=no'],sources=['ftp://xmlsoft.org/%{name}/%{name}-%{version}.tar.gz'])
	def prep(A):
		Package.prep(A)
		if Package.profile.name=='darwin':
			for B in range(1,len(A.local_sources)):A.sh('patch -p1 < "%{local_sources['+str(B)+']}"')
A()