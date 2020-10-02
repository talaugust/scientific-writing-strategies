# -*- coding: utf-8 -*-

from scrapy.linkextractors import LinkExtractor
from scrapy.exceptions import DropItem
import json
import uuid
import os.path

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class SciArticlesPipeline(object):
    def process_item(self, item, spider):
        # test to add an item
        item['article_id'] = str(uuid.uuid4())

        return item



class DuplicatesPipeline(object):

    def __init__(self):
        self.urls_seen = set()

    def process_item(self, item, spider):
        if item['url'] in self.urls_seen:
            raise DropItem("Duplicate item found: %s" % item)
        else:
            self.urls_seen.add(item['url'])
            return item

class JsonWriterPipeline(object):

    def open_spider(self, spider):

        # open and get set of all current articles
        self.existing_files = set()
        self.file_path = 'responses/v2items.jl'
        if os.path.exists(self.file_path):
            article_file = open(self.file_path, 'r')
            for line in article_file:
                article = json.loads(line)
                self.existing_files.add((article['title'], article['site'])) # TODO make this more robust
            article_file.close()
    
        if os.path.exists(self.file_path):
            self.file = open(self.file_path, 'a')
        else: 
            self.file = open(self.file_path, 'w+')
            
        

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        key = (item['title'], item['site'])
        if (key in self.existing_files):
            raise DropItem("Duplicate item found: %s" % item)
        line = json.dumps(dict(item)) + "\n"
        self.file.write(line)
        return item