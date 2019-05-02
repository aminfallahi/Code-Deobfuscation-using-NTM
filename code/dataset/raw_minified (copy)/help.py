A=print
from webtools.management.base import Command as B
class C(B):
	'\n    Show all available commands and these description.\n    '
	def take_action(D,options):
		A('Available commands:');E=D.cmdapp.manager._load_commands()
		for (B,F) in E.items():
			C=F.get_description()
			if C:A('- {0}: {1}'.format(B,C))
			else:A('- {0}'.format(B))