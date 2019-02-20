# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AnjukeItem(scrapy.Item):
    name = scrapy.Field()  # 楼盘名称
    price = scrapy.Field()  # 楼盘单价
    houseType = scrapy.Field()  # 在销售户型
    addr = scrapy.Field()  # 楼盘地址
    startTime = scrapy.Field()  # 开盘时间
    endTime = scrapy.Field()  # 交房时间
    # time = scrapy.Field()  # 开盘时间
