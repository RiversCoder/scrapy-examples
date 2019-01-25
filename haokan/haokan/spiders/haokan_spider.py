# -*- coding: utf-8 -*-
import scrapy
import re
from haokan.items import HaokanItem
from selenium import webdriver
from selenium.webdriver import FirefoxOptions

class HaokanspiderSpider(scrapy.Spider):

    name = 'haokan_spider'
    allowed_domains = ['baijiahao.baidu.com']

    # https://www.pearvideo.com/search_loading.jsp?start=20&k=%E6%80%AA%E5%85%BD&sort=
    start_urls = ['https://baijiahao.baidu.com/u?app_id=1614655764535917&fr=bjhvideo']

    start_page = 0
    page_per = 10
    all_page = 5
    home_page = 'https://www.pearvideo.com/'
    xigua_item = ''
    onoff = False

    def __init__(self):
        super(HaokanspiderSpider, self).__init__(name='haokan_spider')
        option = FirefoxOptions()
        option.headless = True
        self.driver = webdriver.Firefox(options=option)

    def parse(self, response):
        print(response.text)
        video_list = response.xpath("//li")
        for vt in video_list:
            xigua_item = HaokanItem()
            self.xigua_item = xigua_item

            xigua_item['file_url'] = vt.xpath('.//div[@class="largevideo-box"]/@data-src').extract_first()
            xigua_item['file_name'] = vt.xpath('./@data-title').extract_first()
            xigua_item['file_like'] = vt.xpath('.//div[@class="like-num"]/@data-num').extract_first()
            xigua_item['file_author'] = response.xpath('//div[@class="name-item"]//div[@class="name"]/text()').extract_first()
            xigua_item['file_play'] = vt.xpath('.//span[@class="pv"]/text()').extract_first()
            yield xigua_item

    def parse2(self, response):
        self.start_page+=1
        video_list = response.xpath("//li")

        for vt in video_list:
            xigua_item = HaokanItem()
            self.xigua_item = xigua_item
            xigua_item['file_home_url'] = self.home_page + vt.xpath("//div[@class='list-right']/a/@href").extract_first()
            xigua_item['file_name'] = vt.xpath(".//img/@alt").extract_first()
            xigua_item['file_like'] = vt.xpath(".//div[@class='column-info']//span/text()").extract_first()
            xigua_item['file_intro'] = vt.xpath(".//div[@class='cont']/text()").extract_first()
            xigua_item['file_author'] = vt.xpath(".//div[@class='column-info']/a/text()").extract_first()
            xigua_item['file_author_homepage'] = self.home_page + vt.xpath(".//div[@class='column-info']/a/@href").extract_first()
            xigua_item['file_time'] = vt.xpath(".//div[@class='publish-time']/text()").extract_first()

            # 解析整个视频链接
            # yield scrapy.Request(xigua_item['file_home_url'], callback=self.parse_content_page) #callback=
            yield xigua_item

        if (self.start_page < self.all_page):
            yield scrapy.Request('https://www.pearvideo.com/search.jsp?start=' + str(self.page_per * self.start_page) + '&k=%E9%87%8E%E5%85%BD', callback=self.parse)

        print(self.start_page, self.all_page)
        #pass


