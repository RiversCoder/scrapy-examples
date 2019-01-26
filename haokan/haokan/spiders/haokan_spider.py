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

    """""
    
        动物相关：
    
        亲爱的小兔：1590725287278624 （7.6万粉丝  8919万播放 1463视频 结尾7秒处有节目制作信息 更新频率高）
        动物之道：1603848993632982 （9030粉丝 227万播放 89视频 前后片头 右下角有logo水印 更新频率高）
        小虎说动物：1594429776437008（3.6万粉丝 3125万播放 1011视频 前片头后推广 更新频率高）
        趣谈动物：1603266888791577 （4222粉丝 148万播放 50视频 前后片头推广 右下叫logo图标 更新频率高）
        动物视听：603617351377468 （8645粉丝 421万播放 323视频 前后 右下角 更新频率高 男声）
        动物之都：1597640398910970（1.4万粉丝 842万播放 49视频 前片头 更新频率高）
        贪吃动物：1548042592650571 （1.9万粉丝 1008万播放 85视频 左上角LOGO 更新频率一般 男声）
        
        
        小宠宠之家: 1585371786487015 （1.5万粉丝 697万播放 82视频 无水印 更新频率较低）
        动物新天地：1577668344064660 （8713粉丝 465万播放 328视频 无水印 更新频率低）
        动物的家族: 1596449732193287 （8.8万粉丝 9967万播放 857视频 无水印 更新频率高）
        萌猪说动物：1589734860468760 （1.1万粉丝 1283万播放 911视频 无水印 更新频率高）
        宠宠小毛：1579290142391622 （3.4万粉丝 1507万播放 192视频 无水印 更新频率高）
        泡泡萌宠物秀：1613363797288017 （460粉丝 46万播放 112视频 无水印 更新频率高）
        爱狗如家：1596450151398341 （4.7万粉丝 5742播放 792视频 无水印 更新频率高）
        萌宠的趣秀：1593552671010587 （5.2万粉丝 6648万播放 398视频 无水印 更新频率高）*
        趣说的萌宠：1572499273700999（3.6万粉丝 1567万播放 149视频 无水印 更新频率高）*
        宠宠智多星：1579207371485204（7.2万粉丝 3067万视频 121视频 无水印 更新频率高）*
        
    """

    start_urls = [
        'https://baijiahao.baidu.com/u?app_id=1585371786487015&fr=bjhvideo'
        'https://baijiahao.baidu.com/u?app_id=1577668344064660&fr=bjhvideo',
        'https://baijiahao.baidu.com/u?app_id=1596449732193287&fr=bjhvideo',
        'https://baijiahao.baidu.com/u?app_id=1589734860468760&fr=bjhvideo',
        'https://baijiahao.baidu.com/u?app_id=1579290142391622&fr=bjhvideo',
        'https://baijiahao.baidu.com/u?app_id=1613363797288017&fr=bjhvideo',
        'https://baijiahao.baidu.com/u?app_id=1596450151398341&fr=bjhvideo',
        'https://baijiahao.baidu.com/u?app_id=1593552671010587&fr=bjhvideo',
        'https://baijiahao.baidu.com/u?app_id=1572499273700999&fr=bjhvideo',
        'https://baijiahao.baidu.com/u?app_id=1579207371485204&fr=bjhvideo',
    ]

    # start_urls = [
    #     'https://baijiahao.baidu.com/u?app_id=1589734860468760&fr=bjhvideo'
    # ]

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
        # print(response.text)
        video_list = response.xpath("//li")
        for vt in video_list:
            xigua_item = HaokanItem()
            self.xigua_item = xigua_item

            xigua_item['file_url'] = vt.xpath('.//div[@class="largevideo-box"]/@data-src').extract_first()
            xigua_item['file_name'] = vt.xpath('./@data-title').extract_first()
            xigua_item['file_time'] = vt.xpath('.//div[@class="largevideo-tips"]/span[2]/text()').extract_first()
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


