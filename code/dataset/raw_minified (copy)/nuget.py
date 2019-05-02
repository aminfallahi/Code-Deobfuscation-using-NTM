class A(GitHubTarballPackage):
	def __init__(A):GitHubTarballPackage.__init__(A,'mono','nuget','2.8.5','ea1d244b066338c9408646afdcf8acae6299f7fb',configure='')
	def build(A):A.sh('%{make} PREFIX=%{package_prefix}')
	def install(A):A.sh('%{makeinstall} PREFIX=%{staged_prefix}')
A()