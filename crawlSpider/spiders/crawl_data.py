import scrapy
from scrapy_splash import SplashRequest


class Crawl_data(scrapy.Spider):
    name = "crawl_data"
    start_urls = ['https://www.google.co.in/search?q=Republic+Services+in+U.S.&ibp=htl;jobs']

    def start_requests(self):
        yield SplashRequest(self.start_urls[0], self.parse,
            args={'wait': 0.5},
        )

    def parse(self, response):
       # yield {'body':response.body}
		values = response.xpath('//div[@class="nsol9b hxSlV"]').extract()
		list_=[]
		for value in values:
			list_.append(value)

		yield {"List_of_values":list_}
