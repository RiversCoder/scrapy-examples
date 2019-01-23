# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# from scrapy.pipelines.files import FilesPipeline

import os
import requests
import re
from contextlib import closing
BASIC_PATH = 'videos/'
D_PATH = 'D:\\videos\\'
import scrapy

index = 0

class HaokanPipeline(object):


    def __init__(self):
        print('初始化管道')
        self.index = 0
        # self.mkdir(D_PATH + '\\' + '我爱动物世界')

    def process_item(self, item, spider):
        self.data = dict(item)

        if ( int(re.findall(r"\d*", self.data['file_play'])[0]) > 100 or re.search('万', self.data['file_play']) ):
            self.downloads()
            pass
        return item

    def get_file_url(self, response):
        file_urls = re.findall(r"srcUrl=\"(.*?)\"", response.text)
        self.data['file_url'] = file_urls[0]
        self.downloads()

    def downloads(self):
        headers = { "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36" }
        with closing(requests.get(self.data['file_url'], headers=headers, stream=True)) as response:
            chunk_size = 1024  # 单次请求最大值
            content_size = (int(response.headers['content-length'])/chunk_size/chunk_size)  # 内容体总大小
            data_count = 0
            print('\n开始下载:\n')
            # 创建目录
            self.mkdir(D_PATH + '\\' + self.data['file_author'])
            # 开始下载操作
            #with open(BASIC_PATH + self.data['file_author'] + '/' + self.data['file_play'] + ' -- ' + self.data['file_like'] + ' -- ' + self.data['file_name']+'.mp4', 'wb') as file:
            with open(D_PATH + self.data['file_author'] + '\\' + self.data['file_play'] + ' -- ' + self.data['file_like'] + ' -- ' + self.data['file_name'] + '.mp4', 'wb') as file:
                for data in response.iter_content(chunk_size = chunk_size):
                    file.write(data)
                    data_count += (len(data)/chunk_size/chunk_size)
                    now_progress = (data_count / content_size) * 100
                    print("\r 文件下载进度：%d%%(%d M/%d M) - %s " % (now_progress, data_count, content_size, self.data['file_name']), end=" ")
            print('\n\n下载成功!\n')

    def mkdir(self, path):

        print(path)

        # 去除首位空格
        path = path.strip()
        # 去除尾部 \ 符号
        path = path.rstrip("\\")

        # 判断路径是否存在
        # 存在     True
        # 不存在   False
        isExists = os.path.exists(path)

        # 判断结果
        if not isExists:
            # 如果不存在则创建目录
            # 创建目录操作函数
            os.makedirs(path)
            return True
        else:
            # 如果目录存在则不创建，并提示目录已存在
            return False

