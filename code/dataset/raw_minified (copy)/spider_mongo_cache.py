from unittest import TestCase as B
from test.mixin.spider_cache import SpiderCacheMixin as A
class C(B,A):
	def setUp(B):A.setUp(B)
	def setup_cache(A,bot):bot.setup_cache(backend='mongo',database='test_spider')