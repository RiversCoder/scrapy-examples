# -*- coding: utf-8 -*-
import scrapy
from xigua.items import XiguaItem
from selenium import webdriver
from selenium.webdriver import FirefoxOptions

class XiguaspiderSpider(scrapy.Spider):

    name = 'xigua_spider'
    allowed_domains = ['www.pearvideo.com']

    # https://www.pearvideo.com/search_loading.jsp?start=20&k=%E6%80%AA%E5%85%BD&sort=
    start_urls = ['https://www.pearvideo.com/search_loading.jsp?start=20&k=怪兽&sort=']

    start_page = 0
    page_per = 10
    home_page = 'https://www.pearvideo.com/'

    def __init__(self):
        # 在初始化淘宝对象时，创建driver
        super(XiguaspiderSpider, self).__init__(name='xigua_spider')
        option = FirefoxOptions()
        option.headless = True
        self.driver = webdriver.Firefox(options=option)

    def parse(self, response):
        print(response.text)
        video_list = response.xpath("//div[@class='have-result']//li[@class='result-list']")
        print(video_list)
        for vt in video_list:
            xigua_item = XiguaItem()
            xigua_item['file_url'] = self.home_page + vt.xpath("//div[@class='list-right']/a/@href").extract_first()
            xigua_item['file_name'] = vt.xpath(".//h2[@class='tt']").extract_first()
            xigua_item['file_like'] = vt.xpath(".//div[@class='column-info']//span/text()").extract_first()
            xigua_item['file_intro'] = vt.xpath(".//div[@class='cont']/text()").extract_first()
            xigua_item['file_author'] = vt.xpath(".//div[@class='column-info']/a/text()").extract_first()
            xigua_item['file_author_homepage'] = self.home_page + vt.xpath(".//div[@class='column-info']/a/@href").extract_first()
            xigua_item['file_time'] = vt.xpath(".//div[@class='publish-time']/text()").extract_first()
            yield xigua_item

        # print('开启爬取页面')

        # file_urls = re.findall(r"srcUrl=\"(.*?)\"", response.text)
        #
        # for it in file_urls:
        #     xigua_item = XiguaItem()
        #     xigua_item['file_url'] = it
        #     xigua_item['file_name'] = '视频编号' + str(random.randint(1, 100000)) + '.mp4'
        #     yield xigua_item
        #
        # print('结束爬取页面')

        #pass

    # def downloads(self, response, data):
    #     print(data)
    #     f = requests.get(data.file_url)
    #     with open(data.file_name+'.mp4', 'wb') as file:
    #         file.write(f.content)

    # def parse_file(self, response):
