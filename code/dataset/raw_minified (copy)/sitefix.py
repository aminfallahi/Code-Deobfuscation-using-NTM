import sys
from six.moves import builtins as A
def B(builtins):
	"Redefine builtins 'quit' and 'exit' not so close stdin\n\n    "
	def __call__(self,code=None):raise SystemExit(code)
	__call__.__name__='FakeQuitCall';builtins.quit.__class__.__call__=__call__
def C():
	if'site'in sys.modules:B(A)