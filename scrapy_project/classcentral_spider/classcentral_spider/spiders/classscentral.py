# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request

class ClassscentralSpider(scrapy.Spider):
    name = 'classscentral'
    allowed_domains = ['classcentral.com']
    start_urls = ['https://classcentral.com/subjects/']

    def __init__(self, subject=None):
    	self.subject = subject

    def parse(self, response):
    	if self.subject:
    		# values passed as an augument will be replaced at self.subject
    		subject_url = response.xpath('//a[contains(@title, "' + self.subject +'")]/@href').extract_first()
    		absolute_subject_url = response.urljoin(subject_url)
    		yield Request(absolute_subject_url, callback=self.parse_subject)

    	else:
    		self.log('scraping all subjects')
    		subjects = response.xpath('//h3/a[1]/@href').extract()
    		for subject in subjects:
    			absolute_subject_url = response.urljoin(subject)
    			yield Request(absolute_subject_url, callback=self.parse_subject)

    def parse_subject(self, response):
    	subject_name = response.xpath('//h1[@class="head-1"]/text()').extract_first()
    	courses = response.xpath('//tr[@itemtype="http://schema.org/Event"]')
    	for course in courses:
    		course_name = course.xpath('.//*[@itemprop="name"]/text()').extract_first()
    		course_url = response.xpath('.//a[@itemprop="url"]/@href').extract_first()
    		absolute_course_url = response.urljoin(course_url)

    		yield {'subject_name': subject_name,
    				'course_name': course_name,
    				'course_url': course_url }

    	next_page = response.xpath('//link[@rel="next"]/@href').extract_first()
    	if next_page:
    		absolute_next_page = response.urljoin(next_page)
    		yield Request(absolute_next_page, callback=self.parse_subject)