# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

import logging

import aiohttp

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter, is_item
from scrapy import signals


class AuthorizationMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.
    accountpool_url = 'http://127.0.0.1:6789/antispider7/random'
    # authorization = 'jwt eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImFkbWluIiwiZXhwIjoxNzEwNzgwNTg0LCJlbWFpbCI6ImFkbWluQGFkbWluLmNvbSIsIm9yaWdfaWF0IjoxNzEwNzM3Mzg0fQ.0yV8K9ko-LOaiXcr7Jy2gQ85nYWPZAbi58Y1-uS-TdA'
    logger = logging.getLogger('middlewares.authorization')

    async def process_request(self, request, spider):
        async with aiohttp.ClientSession() as client:
            response = await client.get(self.accountpool_url)
            if not response.status == 200:
                return
            credential = await response.text()
            authorization = f'jwt {credential}'
            self.logger.debug(f"set authorization {authorization}")
            request.headers['authorization'] = authorization

class ProxyMiddleware:
    proxypool_url = 'http://localhost:5555/random'
    logger = logging.getLogger('middlewares.proxy')

    async def process_request(self, request, spider):
        async with aiohttp.ClientSession() as client:
            response = await client.get(self.proxypool_url)
            if not response.status == 200:
                return
            proxy = await response.text()
            self.logger.debug(f'set proxy {proxy}')
            request.meta['proxy'] = f'http://{proxy}'
