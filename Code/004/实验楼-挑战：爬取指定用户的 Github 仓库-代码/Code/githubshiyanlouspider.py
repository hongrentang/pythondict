#!/usr/bin/env python3
# _*_ conding:utf-8 _*_

import scrapy

class GithubShiyanlouSpider(scrapy.Spider):
    name = 'shiyanlou-gitub'

    def start_requests(self):
        url_tmp = 'https://github.com/shiyanlou?page={}&tab=repositories'
        urls = (url_tmp.format(i) for i in range(1,4))
        for url in urls:
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self,response):

        for every in response.css('div#user-repositories-list li'):
            yield {
                    "name": every.css('div[class="d-inline-block mb-1"] a::text').extract_first().strip(),
                    "update_time": every.css('relative-time::attr(datetime)').extract_first()
                    
                    }

