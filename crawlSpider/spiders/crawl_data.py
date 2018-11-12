import scrapy
from scrapy_splash import SplashRequest


class Crawl_data(scrapy.Spider):
    name = "crawl_data"
    start_urls = ["https://www.google.co.in/search?q=Republic+Services+in+U.S.&ibp=htl;jobs"]

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse, args={'wait': 0.5})

    def parse(self, response):
        yield {response.body}
