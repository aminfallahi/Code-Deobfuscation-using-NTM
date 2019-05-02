from busbus.provider import ProviderBase as A
from busbus.provider.gtfs import GTFSMixin as B
class C(B,A):
	credit='C-TRAN';credit_url='http://www.c-tran.org/';country='US';gtfs_url='http://www.c-tran.com/images/Google/GoogleTransitUpload.zip'
	def __init__(A,engine=None):super(C,A).__init__(engine,A.gtfs_url)