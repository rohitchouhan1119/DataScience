# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request, FormRequest

class EplanningSpider(scrapy.Spider):
    name = 'eplanning'
    allowed_domains = ['eplanning.ie']
    start_urls = ['http://eplanning.ie/']
    # capture all the urls of country list
    def parse(self, response):
        urls = response.xpath('//a/@href').extract()
        for url in urls:
        	if '#' == url:
        		pass
        	else:
        		yield Request(url+ '/searchtypes', callback = self.parse_application)
    # Capture one urls of planning application list 
    def parse_application(self, response):
    	app_url = response.xpath('//*[@class="glyphicon glyphicon-inbox btn-lg"]/following-sibling::a/@href').extract_first()
    	yield Request(response.urljoin(app_url), callback = self.parse_form)

    # FormRequest will be used here as we are performing action of selecting TimeLimit and click on search. Post request is generate for these actions of a url
    # RdoTimeLimit is the radio button selected
    # formxpath = '(//form)[2])' - it is the section of the form where search is present
    # response - the response containing a HTML form which will be used to pre-populate the form fields
    # formname (string) – if given, the form with name attribute set to this value will be used.
    # formid (string) – if given, the form with id attribute set to this value will be used.
    # formxpath (string) – if given, the first form that matches the xpath will be used.
    # formcss (string) – if given, the first form that matches the css selector will be used.
    # formnumber (integer) – the number of form to use, when the response contains multiple forms. The first one (and also the default) is 0.
    ''' formdata (dict) – fields to override in the form data. If a field was already present in the response <form> element, its value is 
    	overridden by the one passed in this parameter. If a value passed in this parameter is None, the field will not be included in the request,
    	 even if it was present in the response <form> element'''
    '''clickdata (dict) – attributes to lookup the control clicked. If it’s not given, the form data will be submitted simulating a 
    	click on the first clickable element. In addition to html attributes, the control can be identified by its zero-based index 
    	relative to other submittable inputs inside the form, via the nr attribute.'''
    # dont_click (boolean) – If True, the form data will be submitted without clicking in any element.
    # XHR requests are made by javascript code
    # 
    # 
    # 
    # 
    # 


    def parse_form(self, response):
    	yield FormRequest.from_response(response, formdata= { 'RdoTimeLimit': '42'}, dont_filter = True, formxpath = '(//form)[2])', callback = self.parse_pages)

    # 	Get list of url for file number pages
    def parse_pages(self, response):
    	application_urls = response.xpath('//td/a/@href').extract()
    	for url in application_urls:
    		url = response.urljoin(url)
    		yield Request(url, callback = self.parse_items)
    	# It will go to the different pages
    	next_page_url = response.xpath('//*[@rel="next"]').extract_first()
    	absolute_next_page_url = response.urljoin(next_page_url)
    	yield Request(absolute_next_page_url, callback= parse_pages)


    # 
    def parse_items(self, response):
    	agent_btn = response.xpath('//*[@value="Agents"]/@style').extract_first()
        if 'display: inline;  visibility: visible;' in agent_btn:
            name = response.xpath('//tr[th="Name :"]/td/text()').extract_first()

            address_first = response.xpath('//tr[th="Address :"]/td/text()').extract()
            address_second = response.xpath('//tr[th="Address :"]/following-sibling::tr/td/text()').extract()[0:3]

            address = address_first + address_second

            phone = response.xpath('//tr[th="Phone :"]/td/text()').extract_first()

            fax = response.xpath('//tr[th="Fax :"]/td/text()').extract_first()

            email = response.xpath('//tr[th="e-mail :"]/td/a/text()').extract_first()

            url = response.url

            yield {'name': name,
                   'address': address,
                   'phone': phone,
                   'fax': fax,
                   'email': email,
                   'url': url}
        else:
            self.logger.info('Agent button not found on page, passing invalid url.')

