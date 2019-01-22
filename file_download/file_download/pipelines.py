# -*- coding: utf-8 -*-
from scrapy.pipelines.files import FilesPipeline
from urlparse import urlparse
from os.path import basename,dirname,join
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class FileDownloadPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
        path=urlparse(request.url).path
        temp=join(basename(dirname(path)),basename(path))
        return '%s/%s' % (basename(dirname(path)), basename(path))

