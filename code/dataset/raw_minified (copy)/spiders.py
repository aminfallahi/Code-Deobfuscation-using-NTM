from __future__ import unicode_literals
from dynamic_scraper.spiders.django_spider import DjangoSpider as A
from open_news.models import NewsWebsite as C,Article as D,ArticleItem as E
class F(A):
	name='article_spider'
	def __init__(A,*G,**B):A._set_ref_object(C,**B);A.scraper=A.ref_object.scraper;A.scrape_url=A.ref_object.url;A.scheduler_runtime=A.ref_object.scraper_runtime;A.scraped_obj_class=D;A.scraped_obj_item_class=E;super(F,A).__init__(A,*G,**B)