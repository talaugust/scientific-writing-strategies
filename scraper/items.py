# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy.item import Item, Field



class SciArticlesItem(scrapy.Item):

    # define the fields for your item here like:
    # name = scrapy.Field()
    title = Field()
    text = Field()
    site = Field()
    article_id = Field()
    url = Field()
    lead = Field()
    
    pass
