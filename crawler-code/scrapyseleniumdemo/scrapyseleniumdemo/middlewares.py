# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

import time

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter, is_item
from scrapy import signals
from scrapy.http import HtmlResponse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class SeleniumMiddleware:
    def process_request(self, request, spider):
        url = request.url
        service = Service(executable_path=r"C:\Scoop\apps\chromedriver\122.0.6261.39\chromedriver.exe")
        browser = webdriver.Chrome(service=service)
        browser.get(url)
        time.sleep(5)  # TODO 这里直接使用time等待，应该使用方法进行显示等待才行
        html = browser.page_source
        browser.close()
        return HtmlResponse(url=request.url,
                            body=html,
                            request=request,
                            encoding='utf-8',
                            status=200)