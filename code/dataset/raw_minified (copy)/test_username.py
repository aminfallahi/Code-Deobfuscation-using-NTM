from social.tests.backends.legacy import BaseLegacyTest as A
class B(A):
	backend_path='social.backends.username.UsernameAuth';expected_username='foobar';response_body='username=foobar';form='\n    <form method="post" action="{0}">\n        <input name="username" type="text">\n        <button>Submit</button>\n    </form>\n    '
	def test_login(A):A.do_login()
	def test_partial_pipeline(A):A.do_partial_pipeline()