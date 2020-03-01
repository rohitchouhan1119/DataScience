# -*- coding: utf-8 -*-
import scrapy


class CrunchbaseSpider(scrapy.Spider):
    name = 'crunchbase'
    allowed_domains = ['crunchbase.com']
    start_urls = ['http://crunchbase.com/']

    def parse(self, response):
        pass
