import factory as A
class B(A.Factory):
	class Meta:model=dict
	id=A.Sequence(lambda n:n);vendor_code=A.Sequence(lambda n:'VENDOR_CODE{0}'.format(n));datatable_code=A.Sequence(lambda n:'DATATABLE_CODE{0}'.format(n));name=A.Sequence(lambda n:'DATATABLE{0}'.format(n))