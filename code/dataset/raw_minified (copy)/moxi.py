D='x86_32'
C='x86_64'
if env.system.platform in('ubuntu','debian'):
	if env.system.arch==C:A='http://c2493362.cdn.cloudfiles.rackspacecloud.com/moxi-server_x86_64_1.6.0.deb'
	elif env.system.arch==D:A='http://c2493362.cdn.cloudfiles.rackspacecloud.com/moxi-server_x86_1.6.0.deb'
elif env.system.platform in('fedora','redhat'):
	if env.system.arch==C:B='http://c2493362.cdn.cloudfiles.rackspacecloud.com/moxi-server_x86_64_1.6.0.rpm'
	elif env.system.arch==D:B='http://c2493362.cdn.cloudfiles.rackspacecloud.com/moxi-server_x86_1.6.0.rpm'