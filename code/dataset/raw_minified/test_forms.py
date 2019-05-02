C='pwd'
from django.core.urlresolvers import reverse as B
from raspberryio.project.tests.base import RaspberryIOBaseTestCase as A
class D(A):
	url_name='profile_update'
	def setUp(A):A.user=A.create_user(data={'username':'test','password':C});A.url=B(A.url_name)
	def test_twitter_handle_on_form(A):A.client.login(username=A.user.username,password=C);B=A.client.get(A.url);D='<input type="text" placeholder="Twitter Id" name="twitter_id" id="id_twitter_id" />';A.assertContains(B,D,html=True)