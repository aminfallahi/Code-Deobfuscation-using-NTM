import re
from scrapy.selector import Selector as C
from android_apps_crawler.items import AppItem as D
def A(response):
	E="//div[@class='detail_down']/a/@onclick";A=[];F=C(response)
	for G in F.xpath(E).extract():id=re.search('\\d+',G).group();H='http://www.anzhi.com/dl_app.php?s=%s&n=5'%(id,);B=D();B['url']=H;A.append(B)
	return A