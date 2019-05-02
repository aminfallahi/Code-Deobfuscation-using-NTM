from busbus.provider import ProviderBase as A
from busbus.provider.gtfs import GTFSMixin as B
class C(B,A):
	credit='Lawrence Transit';credit_url='http://www.lawrencetransit.org/';country='US';gtfs_url='http://lawrenceks.org/assets/gis/google-transit/google_transit.zip'
	def __init__(A,engine=None):super(C,A).__init__(engine,A.gtfs_url)