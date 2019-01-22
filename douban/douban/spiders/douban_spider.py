# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem

class DoubanSpiderSpider(scrapy.Spider):
    # 爬虫的名字
    name = 'douban_spider'
    # 允许的域名
    allowed_domains = ['movie.douban.com']
    # 入口url
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        movie_list = response.xpath('//div[@class="article"]//ol[@class="grid_view"]/li')
        for it in movie_list:
            douban_item = DoubanItem()
            douban_item['serial_number'] = it.xpath(".//div[@class='item']//em/text()").extract_first()
            douban_item['movie_name'] = it.xpath('.//div[@class="hd"]//a/span[1]/text()').extract_first()
            content = it.xpath('.//div[@class="bd"]//p[1]/text()').extract()
            for c_introduce in content:
                douban_item['introduce'] = "".join(c_introduce.split())
            douban_item['star'] = it.xpath('.//div[@class="star"]/span[@class="rating_num"]/text()').extract_first()
            douban_item['evaluate'] = it.xpath('.//div[@class="star"]/span[4]/text()').extract_first()
            douban_item['describe'] = it.xpath('.//p[@class="quote"]/span/text()').extract_first()
            print(douban_item)
            yield douban_item
        next_link = response.xpath('//span[@class="next"]/a/@href').extract()
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request("https://movie.douban.com/top250"+next_link, callback=self.parse)