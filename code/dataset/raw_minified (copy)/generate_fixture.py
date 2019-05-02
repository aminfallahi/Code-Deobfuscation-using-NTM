'\nPatch database setup for fixture generation so it runs South migrations.\n\n'
from fixture_generator.management.commands import generate_fixture as A
from south.management.commands import patch_for_test_db_setup as B
class C(A.Command):
	def handle(A,*D,**E):B();super(C,A).handle(*D,**E)