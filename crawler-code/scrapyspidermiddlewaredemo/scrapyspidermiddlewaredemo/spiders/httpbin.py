from typing import Iterable

import scrapy
from scrapy import Request


class DemoItem(scrapy.Item):
    origin = scrapy.Field()
    headers = scrapy.Field()
    args = scrapy.Field()
    url = scrapy.Field()

class HttpbinSpider(scrapy.Spider):
    name = "httpbin"
    allowed_domains = ["www.httpbin.org"]
    start_urls = ["https://www.httpbin.org/get"]

    def start_requests(self) -> Iterable[Request]:
        for i in range(5):
            url = f'{self.start_urls[0]}?query={i}'
            yield Request(url)

    def parse(self, response):
        item = DemoItem(**response.json())
        yield item
