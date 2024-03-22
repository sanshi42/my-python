import json
from typing import Iterable

from scrapy import Request, Spider
from scrapy.http import Response
from ScrapyCompositeDemo.items import BookItem


class BookSpider(Spider):
    name = "book"
    allowed_domains = ["antispider7.scrape.center"]
    start_urls = ["https://antispider7.scrape.center"]
    max_page = 512

    def parse_index(self, response):
        data = json.loads(response.text)
        results = data.get('results', [])
        for result in results:
            id = result.get('id')
            url = f'{self.start_urls[0]}/api/book/{id}'
            yield Request(url, callback=self.parse_detail, priority=2)

    def start_requests(self) -> Iterable[Request]:
        for page in range(1, self.max_page + 1):
            url = f'{self.start_urls[0]}/api/book/?limit=18&offset={(page-1)*18}'
            yield Request(url, callback=self.parse_index)

    def parse_detail(self, response):
        data = json.loads(response.text)
        item = BookItem()
        for field in item.fields:
            item[field] = data.get(field)
        yield item
