from __future__ import unicode_literals
B=len
from scraper.scraper_test import ScraperTest as A
class C(A):
	def test_scraper_get_scrape_elems(A):A.assertEqual(B(A.scraper.get_scrape_elems()),4)
	def test_scraper_get_mandatory_scrape_elems(A):A.assertEqual(B(A.scraper.get_mandatory_scrape_elems()),3)