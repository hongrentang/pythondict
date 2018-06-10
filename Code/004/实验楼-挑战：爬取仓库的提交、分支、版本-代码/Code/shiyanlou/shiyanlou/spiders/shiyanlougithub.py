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
            item = GithubItem()
            item['name'] = every.css('div[class="d-inline-block mb-1"] a::text').extract_first().strip()
            item['update_time'] = every.css('relative-time::attr(datetime)').extract_first()
            every_url = response.urljoin(every.css('div[class="d-inline-block mb-1"] a::attr(href)').extract_first())
            request = scrapy.Request(every_url,callback=self.sub_parse)
            request.meta['item'] = item
            yield request

    def sub_parse(self,response):
        item = response.meta['item']
        item['commits'] = response.xpath('//ul[@class="numbers-summary"]/li[1]/a/span/text()').extract_first().strip()
        item['branches'] = response.xpath('//ul[@class="numbers-summary"]/li[2]/a/span/text()').extract_first().strip()
        item['releases'] = response.xpath('//ul[@class="numbers-summary"]/li[3]/a/span/text()').extract_first().strip()

        yield item
