# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html
import random

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter, is_item
from scrapy import signals
from scrapy.http import HtmlResponse


class RandomUserAgentMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.
    user_agents = [
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
        'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.16 (KHTML, like Gecko) Chrome/10.0.648.133 Safari/534.16',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    ]

    def process_request(self, request, spider):
        request.headers['User-Agent'] = random.choice(self.user_agents)
        # return request

# class ProxyMiddleware:

#     def process_request(self, request, spider):
        # request.meta['proxy'] = 'http://203.184.132.103:7890'
        # return HtmlResponse(
        #     url=request.url,
        #     status=200,
        #     encoding='utf-8',
        #     body='Test Downloader Middleware'
        # )

class ChangeResponseMiddleware:
    def process_response(self, request, response, spider):
        response.status = 201
        return response