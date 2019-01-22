# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# from scrapy.pipelines.files import FilesPipeline

import requests
from contextlib import closing

BASIC_PATH = 'videos/'

class XiguaPipeline(object):


    def __init__(self):
        print('初始化管道')

    def process_item(self, item, spider):
        self.data = dict(item)
        print(self.data)
        # self.downloads()
        return item

    def downloads(self):
        headers = { "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36" }
        with closing(requests.get(self.data['file_url'], headers=headers, stream=True)) as response:
            chunk_size = 1024  # 单次请求最大值
            content_size = (int(response.headers['content-length'])/chunk_size/chunk_size)  # 内容体总大小
            data_count = 0
            print('\n开始下载:\n')
            with open(BASIC_PATH + '' + self.data['file_name'], 'wb') as file:
                for data in response.iter_content(chunk_size = chunk_size):
                    file.write(data)
                    data_count += (len(data)/chunk_size/chunk_size)
                    now_progress = (data_count / content_size) * 100
                    print("\r 文件下载进度：%d%%(%d M/%d M) - %s " % (now_progress, data_count, content_size, self.data['file_name']), end=" ")
            print('\n\n下载成功!\n')


