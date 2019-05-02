C=hasattr
import unittest as A
from mock import Mock
from contextio.lib.resources.oauth_provider import OauthProvider as D
class B(A.TestCase):
	def test_constructor_creates_message_object_with_all_attributes_in_keys_list(A):E='provider_consumer_key';B=D(Mock(),{E:'foobar'});A.assertTrue(C(B,'type'));A.assertTrue(C(B,E));A.assertTrue(C(B,'provider_consumer_secret'));A.assertTrue(C(B,'resource_url'))