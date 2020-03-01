# -*- coding: utf-8 -*-
import scrapy
import json

class TweetsSpider(scrapy.Spider):
    name = 'tweets'
    allowed_domains = ['trumptwitterarchive.com']
    start_urls = ['http://d5nxcu7vtzvay.cloudfront.net/data/realdonaldtrump/2009.json',
    			  'http://d5nxcu7vtzvay.cloudfront.net/data/realdonaldtrump/2010.json',
    			  'http://d5nxcu7vtzvay.cloudfront.net/data/realdonaldtrump/2011.json']

    def parse(self, response):
        jsonresponse = json.loads(response.body)
        for tweet in jsonresponse:
        	yield{'created_at': tweet['created_at'], 
		        	'favorite_count': tweet['favorite_count'], 
		        	'id_str': tweet['id_str'],
		         	'is_retweet': tweet['is_retweet'], 
		        	'source': tweet['source'], 
		        	'text': tweet['text']  
        	}
 