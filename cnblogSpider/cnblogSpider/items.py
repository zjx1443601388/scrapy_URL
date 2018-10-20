# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CnblogspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    link = scrapy.Field() # 链接
    start_link = scrapy.Field()
    hash_start_link = scrapy.Field()
    from_link = scrapy.Field()
    out_link = scrapy.Field()
    inner_link = scrapy.Field()
    layer = scrapy.Field()
    out_link_hash = scrapy.Field()
    inner_link_hash = scrapy.Field()
    type1 = scrapy.Field()


class JiandanItem(scrapy.Item):
#    define the fields for your item here like:
    image_urls = scrapy.Field()#图片的链接
