"\nAPI versioning file; we can tell what kind of migrations things are\nby what class they inherit from (if none, it's a v1).\n"
from south.utils import ask_for_it_by_name as B
class A:
	def gf(A,field_name):'Gets a field by absolute reference.';return B(field_name)
class C(A):0
class D(A):no_dry_run=True