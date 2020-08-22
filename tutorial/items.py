# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
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
    #時間戳
    timer = scrapy.Field()
    #價格（$）
    value = scrapy.Field()
    #相對比特幣價格
    bitValue = scrapy.Field()
    #流通市值
    allValue = scrapy.Field()
    #成交額
    tradeValue = scrapy.Field()
    pass
