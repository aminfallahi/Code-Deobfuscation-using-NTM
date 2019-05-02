from django.test import TestCase as A
from inline_media.conf import settings as B
from inline_media.utils import remove_tags as C
class D(A):
	def test_remove_tags(A):D='<p>Es war<br>einmal</br>und andere</br>geschichte</p>';E='<p>Es war<br>einmal und andere geschichte</p>';A.assertEqual(C(D,B.INLINE_MEDIA_REMOVE_TAGS),E)