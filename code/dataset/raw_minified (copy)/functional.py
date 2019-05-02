from __future__ import absolute_import
from django.utils.functional import empty
def A(lo):
	"\n    Unwrap a LazyObject and return the inner object. Whatever that may be.\n\n    ProTip: This is relying on `django.utils.functional.empty`, which may\n    or may not be removed in the future. It's 100% undocumented.\n    ";A=lo
	if not hasattr(A,'_wrapped'):return A
	if A._wrapped is empty:A._setup()
	return A._wrapped