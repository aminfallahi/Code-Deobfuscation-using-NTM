from django.core.management.base import BaseCommand as A,CommandError as B
from olympia.amo.utils import chunked as C
from olympia.files.tasks import fix_let_scope_bustage_in_addons as D
class E(A):
	args='<addon_id addon_id ...>';help='Fix the "let scope bustage" (bug 1224686) for a list of add-ons.\nOnly the last version of each add-on will be fixed, and its version bumped.'
	def handle(G,*A,**H):
		if len(A)==0:raise B('Please provide at least one add-on id to fix.')
		E=[int(B)for B in A]
		for F in C(E,100):D.delay(F)