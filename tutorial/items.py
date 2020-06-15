# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class TutorialItem(scrapy.Item):
    link = scrapy.Field()
    body = scrapy.Field()

class article(scrapy.Item):
    title = scrapy.Field()
    parrafo = scrapy.Field()

#class TutorialItem(scrapy.Item):
#    # define the fields for your item here like:
#    # name = scrapy.Field()
#    title = scrapy.Field()
#    link = scrapy.Field()

#class article(scrapy.Item):
    #title = scrapy.Field()
    #parrafo = scrapy.Field()