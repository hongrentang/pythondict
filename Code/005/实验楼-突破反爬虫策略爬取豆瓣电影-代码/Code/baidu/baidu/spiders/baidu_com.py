# -*- coding: utf-8 -*-
import scrapy
from baidu.items import PageItem
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule



class BaiduComSpider(scrapy.spiders.CrawlSpider):
    name = 'baidu_com'
    allowed_domains = ['movie.douban.com']
    start_urls = ['https://movie.douban.com/subject/3011091/']

    rules = (
            Rule(LinkExtractor(restrict_xpaths=('//div[@class="recommendations-bd"]')),callback='parse_move',follow=True),
            )

    def parse_move(self, response):
        item = PageItem()
        print(response.url)
        item['url'] = str(response.url)
    
            
        yield item
