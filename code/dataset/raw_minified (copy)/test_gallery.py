_A='http://127.0.0.1:8000/photo-gallery/'
from .base import *
class GalleryPageTests(SeleniumTestCase):
	def test_gallery_items(self):browser=self.browser;browser.get(_A);assert"we don't have any Galleries"not in browser.page_source
	def test_gallery_images(self):browser=self.browser;browser.get(_A);link=browser.find_element_by_class_name('th');link.click();assert'No images are tagged'not in browser.page_source