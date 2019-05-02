from django.db.models import IntegerField as A,Transform as B
class C(B):
	lookup_name='level';function='nlevel'
	@property
	def output_field(self):return A()