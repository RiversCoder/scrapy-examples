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

    # def __init__(self):
        # 在初始化淘宝对象时，创建driver
        # super(XiguaspiderSpider, self).__init__(name='xigua_spider')
        # option = FirefoxOptions()
        # option.add_argument("authority='www.pearvideo.com'")
        # option.add_argument("scheme=https")
        # option.add_argument("referer='https://www.pearvideo.com/search.jsp?start=0&k=%E6%80%AA%E5%85%BD'")
        # option.add_argument("user-agent='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'")
        # option.add_argument("x-requested-with='XMLHttpRequest'")
        #option.headless = True
        # profile = webdriver.FirefoxProfile()
        # profile.set_preference("general.useragent.override", "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36")
        # self.driver = webdriver.Firefox(options=option)
        # self.driver.header_overrides = {
        #     'authority': 'www.pearvideo.com',
        #     'scheme': 'https',
        #     'referer': 'https://www.pearvideo.com/search.jsp?start=0&k=%E6%80%AA%E5%85%BD',
        #     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
        #     'x-requested-with': 'XMLHttpRequest'
        # }

        # 进入浏览器设置
        # options = webdriver.ChromeOptions()
        # # 设置中文
        # options.add_argument('lang=zh_CN.UTF-8')
        # # 更换头部
        # # options.add_argument('user-agent="Mozilla/5.0 (iPod; U; CPU iPhone OS 2_1 like Mac OS X; ja-jp) AppleWebKit/525.18.1 (KHTML, like Gecko) Version/3.1.1 Mobile/5F137 Safari/525.20"')
        # options.add_argument("authority='www.pearvideo.com'")
        # options.add_argument("scheme=https")
        # options.add_argument("referer='https://www.pearvideo.com/search.jsp?start=0&k=%E6%80%AA%E5%85%BD'")
        # options.add_argument("user-agent='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36'")
        # options.add_argument("x-requested-with='XMLHttpRequest'")
        # self.driver = webdriver.Chrome(chrome_options=options)

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

            # 解析整个视频链接
            # yield scrapy.Request(xigua_item['file_home_url'], callback=self.parse_content_page) #callback=
            yield xigua_item

        if (self.start_page < self.all_page):
            yield scrapy.Request('https://www.pearvideo.com/search.jsp?start=' + str(self.page_per * self.start_page) + '&k=%E9%87%8E%E5%85%BD', callback=self.parse)

        print(self.start_page, self.all_page)
        #pass


    def parse_content_page(self, response):

        print('开启爬取视频详情页面')

        file_urls = re.findall(r"srcUrl=\"(.*?)\"", response.text)
        self.xigua_item['file_url'] = file_urls[0]
        yield self.xigua_item

        # for it in file_urls:
            # xigua_item = XiguaItem()

            # xigua_item['file_name'] = '视频编号' + str(random.randint(1, 100000)) + '.mp4'

        self.onoff = True
        print('结束爬取视频详情页面')

