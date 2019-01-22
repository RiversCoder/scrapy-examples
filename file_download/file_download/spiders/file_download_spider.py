# -*- coding:UTF-8 -*- ＃
from scrapy.spiders import Spider,CrawlSpider,Rule
from scrapy.selector import Selector
from scrapy.http import Request
from scrapy import FormRequest
from file_download.items import FileDownloadItem
from scrapy.utils.response import open_in_browser
from scrapy.linkextractors import LinkExtractor
from bs4 import BeautifulSoup
import sys
import re
import os

from urlparse import urlparse
from urlparse import urlunparse

class fileSpider(Spider):
    name="file_download"
    allowed_domains=['matplotlib.org']
    start_urls=['http://matplotlib.org/examples/index.html']
    def parse(self,response):
        le=LinkExtractor(restrict_xpaths='//*[@id="matplotlib-examples"]/div',deny='/index.html$')
        for link in le.extract_links(response):
            yield Request(link.url,callback=self.parse_link)
    def parse_link(self,response):
        pattern = re.compile('href=(.*\.py)')
        div=response.xpath('/html/body/div[4]/div[1]/div/div')
        p=div.xpath('//p')[0].extract()
        link=re.findall(pattern,p)[0]
        if ('/') in link:
            href='http://matplotlib.org/'+link.split('/')[2]+'/'+link.split('/')[3]+'/'+link.split('/')[4]
        else:
            link=link.replace('"','')
            scheme=urlparse(response.url).scheme
            netloc=urlparse(response.url).netloc
            temp=urlparse(response.url).path
            path='/'+temp.split('/')[1]+'/'+temp.split('/')[2]+'/'+link
            combine=(scheme,netloc,path,'','','')
            href=urlunparse(combine)
#            print href,os.path.splitext(href)[1]
        file=FileDownloadItem()
        file['file_urls']=[href]
        return file

