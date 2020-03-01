# -*- coding: utf-8 -*-
import scrapy


class CarSpidersSpider(scrapy.Spider):
    name = 'car_spiders'
    allowed_domains = ['baierl.com']
    start_urls = ['http://baierl.com/']

    def parse(self, response):
        pass
