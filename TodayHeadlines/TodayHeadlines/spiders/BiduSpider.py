# -*- coding: utf-8 -*-
import scrapy

class BiduspiderSpider(scrapy.Spider):

    name = 'BiduSpider'
    allowed_domains = ['http://blog.sina.com.cn/']
    start_urls = ['http://blog.sina.com.cn/riversfrog']

    def parse(self, response):
        print('123321')
        filename = response.url.split('/')[-2]
        with open(filename, 'wb') as f:
            f.write(response.data)
        # pass
