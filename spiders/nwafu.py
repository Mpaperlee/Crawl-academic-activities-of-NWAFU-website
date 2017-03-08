#!/usr/bin/env python
# encoding: utf-8

import scrapy
from nwafu.items import NwafuItem
import logging

class nwafuSpider(scrapy.Spider):
    name = "nwafu"
    allowed_domains = ["nwsuaf.edu.cn"]
    start_urls = [
        "http://www.nwsuaf.edu.cn/xshd/index.htm"
    ]
    def parse(self,response):
        news_page_num = 19
        page_num = 25
        if response.status == 200:
            for i in range(1,page_num - 1):
                for j in range(0,news_page_num):
                    item = NwafuItem()
                    item['news_url'] = response.xpath("//*[@class='main_content']/table[1]/tr/td/ul/li/a/@href").extract()[j]
                    item['news_title'] = response.xpath("//*[@class='main_content']/table[1]/tr/td/ul/li/a/text()").extract()[j]
                    item['news_date'] = response.xpath("//*[@class='main_content']/table[1]/tr/td/ul/li/span/text()").extract()[j]
                    yield item
                nextpage_url = "http://www.nwsuaf.edu.cn/xshd/%sindex.htm" % i
                yield scrapy.Request(nextpage_url,callback = self.parse_news)
    def parse_news(self, respons):
        """TODO: Docstring for parse_news.
        :returns: TODO

        """
        news_page_num = 19
        if response.status == 200:
            for i in range(1, news_page_num):
                item = NwafuItem()
                item['news_url'] = response.xpath("//*[@class='main_content']/table[1]/tr/td/ul/li/a/@href").extract()[i]
                item['news_title'] = response.xpath("//*[@class='main_content']/table[1]/tr/td/ul/li/a/a/text()").extract()[i]
                item['news_date'] = response.xpath("//*[@class='main_content']/table[1]/tr/td/ul/li/span/text()").extract()[i]
                yield item

