# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class HaitaoItem(scrapy.Item):
    # define the fields for your item here like:
    image = scrapy.Field()
    href = scrapy.Field()
    name = scrapy.Field()
    cost = scrapy.Field()
    # name = scrapy.Field()
    # name = scrapy.Field()
    # chName = scrapy.Field()
    # href = scrapy.Field()
    # value = scrapy.Field()
    # globalIndex = scrapy.Field()
    # value24h = scrapy.Field()
    # number = scrapy.Field()
    # change = scrapy.Field()
    # increase = scrapy.Field()
    pass
