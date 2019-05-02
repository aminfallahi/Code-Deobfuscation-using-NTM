'\n    flask_storage.contrib.sae\n    ~~~~~~~~~~~~~~~~~~~~~~~~~\n\n    Storage for SAE backend.\n'
from ._base import BaseStorage as A
from ._utils import ConfigItem as B
class C(A):
	bucket=B('STORAGE_SAE_BUCKET')
	def save(A):0