import os
from ..command import Command as A
class B(A):
	def _get_migration_path(A):return os.path.join(os.getcwd(),'migrations')