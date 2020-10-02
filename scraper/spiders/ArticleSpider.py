# Super class for all the scraping spiders for scientific articles, blogs, etc. 
# pretty simple class, just keep a constant link exteactor for study links, and the same item for all pipelines
import os
import sys
sys.path.append(os.getcwd())


import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from items import SciArticlesItem
import logging


# Single spider class for all spiders, pass in params for getting the correct xpaths and 
# rules for scraping each site. Examples are in runSpiders.pys
class ArticleSpider(CrawlSpider):
    name = 'article_spider'
    allowed_domains = [] 
    start_urls = []
    rules = []

    def __init__(self, *args, **kwargs):
        self.item_constr = SciArticlesItem

        self.allowed_domains = kwargs['domains']
        self.start_urls = kwargs['urls']

        # note that these are lists, if the first returns none, we continue to the next
        self.xpath_title = kwargs['xpath_title']
        self.xpath_body = kwargs['xpath_body']
        allow = kwargs.get('article_extension', [])
        deny = kwargs.get('deny_extension', [])
        self.rules = [Rule(LinkExtractor(allow=allow, deny=deny), callback='parse_item')]

        super().__init__(*args, **kwargs)

    def parse_site(self, response):
        return response.url.split('/')[2]

    def parse_xpath(self, xpaths, response):
        text = None
        for xpath in xpaths:
            text = response.xpath(xpath)
            if len(text) > 0:
                break
            self.logger.info("no text found, going to next xpath")

        if text is not None:
            # the first xpath gets a bunch of selectors, and this one now selects all the text
            return [s.xpath('string(.)').get() for s in text] 
        else:
            return None

    def parse_item(self, response):
        item = self.item_constr()

        item['url'] = response.url
        item['title']= self.parse_xpath(self.xpath_title, response)
        item['text'] = self.parse_xpath(self.xpath_body, response)
        item['lead'] = self.parse_xpath(self.xpath_lead, response)

        item['site'] = self.parse_site(response)

        return item



