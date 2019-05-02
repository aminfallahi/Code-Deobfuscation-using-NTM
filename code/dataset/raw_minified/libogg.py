class A(XiphPackage):
	def __init__(A):XiphPackage.__init__(A,project='ogg',name='libogg',version='1.3.0');A.configure='autoreconf -fi && ./configure --prefix="%{prefix}"';A.sources.append('patches/libogg-opt.patch')
	def prep(A):Package.prep(A);A.sh('patch -p1 < "%{local_sources[1]}"')
A()