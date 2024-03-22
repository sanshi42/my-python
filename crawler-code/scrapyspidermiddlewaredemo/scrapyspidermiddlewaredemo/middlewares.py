# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter, is_item
from scrapy import signals


class CustomizeMiddleware:

    def process_spider_input(self, response, spider):
        response.status = 201

    def process_spider_output(self, response, result, spider):
        for i in result:
            # if isinstance(i, De)
            i['origin'] = None
            yield i


    def process_start_requests(self, start_requests, spider):
        for request in start_requests:
            url = request.url
            url += '&name=germy'
            request = request.replace(url=url)
            yield request