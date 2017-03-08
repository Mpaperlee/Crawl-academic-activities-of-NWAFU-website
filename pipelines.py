# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
import json

class NwafuPipeline(object):
    def __init__(self):
        self.file = open('nwafu.txt' , 'w')
    def process_item(self, item, spider):
        self.file.write(item['news_title']+item['news_date']+'\n'+"nwsuaf.edu.cn/xshd/"+item['news_url']+'\n')
        #self.file.write("\n")
        #self.file.write(item['news_date'])
        #self.file.write("\n")
        #self.file.write("nwsuaf.edu.cn/xshd/"+item['news_url'])
        #self.file.write("\n")
        return item
