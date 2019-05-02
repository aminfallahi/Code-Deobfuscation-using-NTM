class A(XiphPackage):
	def __init__(A):XiphPackage.__init__(A,project='vorbis',name='libvorbis',version='1.3.2');A.configure='./configure --prefix="%{prefix}"';A.sources.append('patches/libvorbis-opt.patch')
	def prep(A):Package.prep(A);A.sh('patch -p1 < "%{local_sources[1]}"')
A()