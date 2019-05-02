from django.contrib.staticfiles.testing import StaticLiveServerTestCase as A
from django.utils.translation import activate as B
from selenium.webdriver.common.keys import Keys
from selenium import webdriver as C
class D(A):
	def setUp(A):A.browser=C.Firefox();A.browser.implicitly_wait(3);B('en')
	def tearDown(A):A.browser.quit()