from .basetest import BaseTestFilesystemMount as A
class B(A):
	def setUp(A):A.filename='images/test.iso'
	def validate_count(A,volumes):A.assertEqual(len(volumes),1)
	def validate_types(A,volumes):A.assertEqual(volumes[0].fstype,'iso9660')