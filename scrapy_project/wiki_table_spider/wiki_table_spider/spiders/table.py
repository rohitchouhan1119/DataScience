# -*- coding: utf-8 -*-
import scrapy


class TableSpider(scrapy.Spider):
    name = 'table'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/List_of_United_States_cities_by_population']

    def parse(self, response):
        table = response.xpath('//table[contains(@class,"wikitable sortable")]')[0]
        trs = table.xpath('.//tr')[1:]
        for tr in trs:
        	rank = tr.xpath('.//td[1]/text()').extract_first().strip()
        	city = tr.xpath('.//td[2]//text()').extract_first()
        	state = tr.xpath('.//td[3]//text()').extract()[1]
        	estimate = tr.xpath('.//td[4]//text()').extract_first().strip()
        	census = tr.xpath('.//td[5]//text()').extract_first().strip()
        	change = tr.xpath('.//td[6]//text()').extract_first()

        	yield {
					'rank': rank,
					'city': city,
					'state': state,
					'estimate': estimate,
					'census': census,
					'change': change,

        	}

