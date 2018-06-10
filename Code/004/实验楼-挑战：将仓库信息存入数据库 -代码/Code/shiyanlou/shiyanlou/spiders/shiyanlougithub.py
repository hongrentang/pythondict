# -*- coding: utf-8 -*-
import scrapy
from shiyanlou.items import GithubItem


class ShiyanlougithubSpider(scrapy.Spider):
    name = 'shiyanlougithub'
    @property
    def start_urls(self):
        url_tmp = 'https://github.com/shiyanlou?page={}&tab=repositories'
        return (url_tmp.format(i) for i in range(1,4))

    def parse(self, response):
        
        for every in response.css('div#user-repositories-list li'):
            
            item=GithubItem({
                'name': every.css('div[class="d-inline-block mb-1"] a::text').extract_first().strip(),
                'update_time': every.css('relative-time::attr(datetime)').extract_first()
        
                })
            yield item
