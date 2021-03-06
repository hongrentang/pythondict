# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import redis
import re
import json
class DoubanMoviePipeline(object):
    def process_item(self, item, spider):
        score = float(item['score'])
        
        if score > 8.0:
            item['score'] = score
            item['summary'] = re.sub('\s','',item['summary'])
            item = json.dumps(dict(item),ensure_ascii=False)
            self.redis.lpush('douban_movie:items',item)
            return item

    def open_spider(self,spider):
        self.redis = redis.StrictRedis(host='localhost',port=6379,db=0)
