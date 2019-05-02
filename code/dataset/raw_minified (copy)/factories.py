import factory as A
class B(A.django.DjangoModelFactory):
	username=A.Sequence(lambda n:'user-{0}'.format(n));email=A.Sequence(lambda n:'user-{0}@example.com'.format(n));password=A.PostGenerationMethodCall('set_password','password')
	class Meta:model='users.User';django_get_or_create='username',