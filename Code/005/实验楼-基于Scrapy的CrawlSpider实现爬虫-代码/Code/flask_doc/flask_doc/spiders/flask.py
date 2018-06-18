# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from flask_doc.items import PageItem
#import re
class FlaskSpider(CrawlSpider):
    name = 'flask'
    allowed_domains = ['flask.pocoo.org']
    start_urls = ['http://flask.pocoo.org/docs/0.12/']

    rules = (
        Rule(LinkExtractor(allow=('.*#.*')), callback='parse_page',follow=True),
    )
    print(rules)
    def parse_page(self, response):
        print(response.url)
        
        item = PageItem()
        item['url'] = str(response.url)
        item['text'] = response.xpath('//div[@class="body"]').extract_first()
        #item['body'] = re.sub('<.*?>|\s','',body)
        yield item
