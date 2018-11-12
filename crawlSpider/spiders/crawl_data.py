import scrapy
from scrapy_splash import SplashRequest


class Crawl_data(scrapy.Spider):
    name = "crawl_data"
    start_urls = ['http://news.tv-asahi.co.jp/news_society/articles/000089004.html']

    def start_requests(self):
        yield SplashRequest(self.start_urls[0], self.parse,
            args={'wait': 0.5},
        )

    def parse(self, response):
        yield {'body':response.body}

