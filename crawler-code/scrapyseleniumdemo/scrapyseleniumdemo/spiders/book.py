import re
from typing import Iterable

import scrapy
from scrapy import Request, Spider
from scrapy.http import Response
from scrapyseleniumdemo.items import BookItem


class BookSpider(scrapy.Spider):
    name = "book"
    allowed_domains = ["spa5.scrape.center"]
    start_urls = ["https://spa5.scrape.center"]

    def parse_index(self, response):
        """解析列表页"""
        items = response.css('.item')
        for item in items:
            href = item.css('.top a::attr(href)').extract_first()
            detail_url = response.urljoin(href)
            yield Request(detail_url, callback=self.parse_detail, priority=2)

        if match := re.search(r'page/(\d+)', response.url):
            page = int(match.group(1))
            next_url = f'{self.start_urls[0]}/page/{page+1}'
            yield Request(next_url, callback=self.parse_index)


    def parse_detail(self, response: Response):
        name = response.css('.name::text').extract_first()
        tags = response.css('.tags button span::text').extract_first()
        score = response.css('.score::text').extract_first()
        price = response.css('.price span::text').extract_first()
        cover = response.css('.cover::attr(src)').extract_first()
        tags = [tag.strip() for tag in tags] if tags else []
        score = score.strip() if score else None
        item = BookItem(name=name, tags=tags, score=score, price=price, cover=cover)
        yield item


    def start_requests(self) -> Iterable[Request]:
        """定义初始的爬取逻辑"""
        start_url = f'{self.start_urls[0]}/page/1'
        yield Request(start_url, callback=self.parse_index)