D='bar'
C='foo'
import unittest as B
from contextio.contextio import ContextIO as A
from contextio.lib.v2_0 import V2_0
from contextio.lib.lite import Lite
class E(B.TestCase):
	def test_ContextIOFactory_returns_v2_0_instance_by_default(B):E=A(consumer_key=C,consumer_secret=D);B.assertIsInstance(E,V2_0)
	def test_ContextIOFactory_returns_Lite_instance(B):E=A(consumer_key=C,consumer_secret=D,api_version='lite');B.assertIsInstance(E,Lite)