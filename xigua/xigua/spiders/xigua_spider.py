# -*- coding: utf-8 -*-
import scrapy
import re
from xigua.items import XiguaItem
from selenium import webdriver
from selenium.webdriver import FirefoxOptions

class XiguaspiderSpider(scrapy.Spider):

    name = 'xigua_spider'
    allowed_domains = ['www.pearvideo.com']

    # https://www.pearvideo.com/search_loading.jsp?start=20&k=%E6%80%AA%E5%85%BD&sort=
    start_urls = ['https://www.pearvideo.com/search.jsp?start=0&k=%E9%87%8E%E5%85%BD']

    start_page = 0
    page_per = 10
    all_page = 5
    home_page = 'https://www.pearvideo.com/'
    xigua_item = ''
    onoff = False

    def parse(self, response):
        self.start_page+=1
        video_list = response.xpath("//li[@class='result-list']")
        self.onoff = False

        for vt in video_list:
            xigua_item = XiguaItem()
            self.xigua_item = xigua_item
            xigua_item['file_home_url'] = self.home_page + vt.xpath("//div[@class='list-right']/a/@href").extract_first()
            xigua_item['file_name'] = vt.xpath(".//img/@alt").extract_first()
            xigua_item['file_like'] = vt.xpath(".//div[@class='column-info']//span/text()").extract_first()
            xigua_item['file_intro'] = vt.xpath(".//div[@class='cont']/text()").extract_first()
            xigua_item['file_author'] = vt.xpath(".//div[@class='column-info']/a/text()").extract_first()
            xigua_item['file_author_homepage'] = self.home_page + vt.xpath(".//div[@class='column-info']/a/@href").extract_first()
            xigua_item['file_time'] = vt.xpath(".//div[@class='publish-time']/text()").extract_first()

            yield xigua_item

        if (self.start_page < self.all_page):
            yield scrapy.Request('https://www.pearvideo.com/search.jsp?start=' + str(self.page_per * self.start_page) + '&k=%E9%87%8E%E5%85%BD', callback=self.parse)

        print(self.start_page, self.all_page)
        #pass
