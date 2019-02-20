# -*- coding: utf-8 -*-
import scrapy
from anjuke.items import AnjukeItem
from scrapy.http import Request
from scrapy.selector import Selector


class AnjukespiderSpider(scrapy.Spider):
    name = 'anjukeSpider'
    allowed_domains = ['fang.anjuke.com']
    start_urls = ['https://xa.fang.anjuke.com/loupan/all/a1_w1/']

    def parse(self, response):
        selector = Selector(response)
        for each in selector.xpath("//div[@class='infos']"):
            detailUrl = each.xpath("./a[@class='lp-name']/@href").extract()[0]
            yield Request(url=detailUrl, callback=self.parse2)  # 处理响应的回调函数。

        nextUrl = selector.xpath("//a[@class='next-page next-link']/@href").extract()[0]
        if nextUrl is not None:
            yield Request(url=nextUrl, dont_filter=True, callback=self.parse)  # 处理响应的回调函数。

    def parse2(self, response):
        selector = Selector(response)
        item = AnjukeItem()
        try:
            item['name'] = selector.xpath("//div[@class='basic-info']/h1/text()").extract()[0]
        except Exception, e:
            item['name'] = ""
            print e.message
        try:
            item['price'] = selector.xpath("//dd[@class='price']/p/em/text()").extract()[0]
        except Exception, e:
            item['price'] = ""
            print e.message

        # types = []
        try:
            item["houseType"] = \
            selector.xpath("//ul[@class='hx-list']//div[@class='desc-txt clearfix']//span/text()").extract()[0]
        except Exception, e:
            item["houseType"] = ''
            print e.message

        # for type in selector.xpath("//ul[@class='hx-list']//div[@class='desc-txt clearfix']"):
        #     types.append(str(type.xpath("/span/text()").extract()[0]).replace(" ", ""))
        # item["houseType"] = "dsadfasdf"
        try:
            item['addr'] = selector.xpath("//a[@class='lpAddr-text g-overflow']/text()").extract()[0]
        except Exception, e:
            item['addr'] = ''
            print e.message

        try:
            item['startTime'] = selector.xpath("//div[@class='kp-infos']/ul[1]//span/text()").extract_first()
        except Exception as e:
            item['startTime'] = ''

        try:
            item['endTime'] = selector.xpath("//div[@class='kp-infos']/ul[2]//span/text()").extract_first()
        except Exception as e:
            item['endTime'] = ''

        yield item
