import logging as A
from plumbum import local
C=A.getLogger(__name__)
def B(command,dry_run):
	'Executes a shell command unless the dry run option is set';A=command
	if not dry_run:B=A.split(' ');return local[B[0]](B[1:])
	else:C.info('Dry run of %s, skipping'%A)
	return True