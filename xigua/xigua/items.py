# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class XiguaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    file_url = scrapy.Field()
    file_name = scrapy.Field()
    file_like = scrapy.Field()
    file_intro = scrapy.Field()
    file_time = scrapy.Field()
    file_author = scrapy.Field()
    file_author_homepage = scrapy.Field()
    file_home_url = scrapy.Field()

    pass
