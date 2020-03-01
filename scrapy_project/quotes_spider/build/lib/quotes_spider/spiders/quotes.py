# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com/']
    start_urls = ['http://quotes.toscrape.com//']

    def parse(self, response):
        h1_tag = response.xpath('//h1/a/text()').extract_first()
        tags = response.xpath('//*[@class="tag-item"]/a/text()').extract()

        yield {'H1 TAG': h1_tag, 'Tags': tags}

        quotes = response.xpath('//*[@class="quote"]')
        for quote in quotes:
        	text = quote.xpath('.//*[@class="text"]/text()').extract_first()
        	author = quote.xpath('.//*[@itemprop="author"]/text()').extract_first()
        	tags = quote.xpath('.//*[@class="tag"]/text()').extract()

        	yield { 'Text': text,
        			'Author': author,
        			'Tags':tags}
        			
