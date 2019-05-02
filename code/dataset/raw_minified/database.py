import factory as A
class B(A.Factory):
	class Meta:model=dict
	id=A.Sequence(lambda n:n);database_code=A.Sequence(lambda n:'DATABASE_CODE{0}'.format(n));name='National Stock Exchange of India';description='Stock and index data from the National Stock Exchange of India. ';datasets_count=1877;downloads=1800463;premium=False;image='https://s3.amazonaws.com/thumb_nse.png'