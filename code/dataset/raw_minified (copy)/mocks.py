from boto.mturk.connection import MTurkConnection as A
class B(A):
	"\n\tMock MTurkConnection that doesn't connect, but instead just prepares\n\tthe request and captures information about its usage.\n\t"
	def _process_request(A,*B,**C):D=A.__dict__.setdefault('_mock_saved_args',dict());D['_process_request']=B,C