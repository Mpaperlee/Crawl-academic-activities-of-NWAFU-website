#!/usr/bin/env python
# encoding: utf-8

import scrapy
from nwafu.items import NwafuItem

class nwafuSpider(scrapy.Spider):
    name = "nwafu"
    allowed_domains = ["nwsuaf.edu.cn"]
    start_urls = [
        "http://www.nwsuaf.edu.cn/xshd/index.htm"
    ]
    def parse(self,response):
        news_num = 19
        page_num = 25
        if response.status == 200:
            for i in range(1,page_num ):
                for j in range(0,news_num):
                    item = NwafuItem()
                    item['url'] = response.xpath("//*[@class='main_content']/table[1]/tr/td/ul/li/a/@href").extract()[j]
                    item['title'] = response.xpath("//*[@class='main_content']/table[1]/tr/td/ul/li/a/text()").extract()[j]
                    item['date'] = response.xpath("//*[@class='main_content']/table[1]/tr/td/ul/li/span/text()").extract()[j]
                    yield item
                nextpage_url = "http://www.nwsuaf.edu.cn/xshd/%sindex.htm" % i
                yield scrapy.Request(nextpage_url)