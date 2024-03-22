from typing import Iterable

import scrapy
from scrapy import Request
from scrapy.http import FormRequest, JsonRequest


class HttpbinSpider(scrapy.Spider):
    name = "httpbin"
    allowed_domains = ["httpbin.org"]
    start_urls = ["https://httpbin.org/post"]
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
    }
    data = {'name': 'germey', 'age': '26'}

    def start_requests(self) -> Iterable[Request]:
        yield FormRequest(url=self.start_urls[0],
                      callback=self.parse,
                      formdata=self.data)
        yield JsonRequest(url=self.start_urls[0],
                          callback=self.parse,
                          data=self.data)

    def parse(self, response):
        print('url', response.url)
        print('request', response.request)
        print('status', response.status)
        print('headers', response.headers)
        print('text', response.text)
        print('meta', response.meta)