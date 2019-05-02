class A(SourceForgePackage):
	def __init__(A):SourceForgePackage.__init__(A,'%{name}','libjpeg-turbo','1.3.0')
	def arch_build(A,arch):
		C='--host x86_64-apple-darwin NASM=%{prefix}/bin/nasm';B=arch
		if B=='darwin-universal':A.local_configure_flags=[C]
		elif B=='darwin-32':A.local_configure_flags=['--host i686-apple-darwin CFLAGS="-O3 -m32" LDFLAGS=-m32']
		elif B=='darwin-64':A.local_configure_flags=[C]
		Package.arch_build(A,B,defaults=False)
A()