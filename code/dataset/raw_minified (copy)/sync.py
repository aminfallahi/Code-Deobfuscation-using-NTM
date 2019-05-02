A=staticmethod
from ...error import GraphQLError as B
from ...pyutils.defer import Deferred as C
class D:
	@A
	def run_resolve_fn(resolver,original_resolver):
		A=resolver()
		if isinstance(A,C):raise B('You cannot return a Deferred from a resolver when using SynchronousExecutionMiddleware')
		return A
	@A
	def execution_result(executor):A=executor();return A.result