# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest

class BaierlSpider(scrapy.Spider):
    name = 'baierl'
    allowed_domains = ['baierl.com']
    start_urls = ['https://baierl.com/new-inventory/']

    def parse(self, response):
        pass
