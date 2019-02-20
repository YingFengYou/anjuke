# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymongo
import datetime
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class AnjukePipeline(object):

    def __init__(self):
        self.clinet = pymongo.MongoClient("localhost", 27017)
        self.db = self.clinet["Anjuke"]
        self.AnjukeItem = self.db["AnjukeInfo"]

    def process_item(self, item, spider):
        dt = datetime.datetime.now()
        if (len(item['name']) > 0):
            house_info = {}
            house_info["house_name"] = item['name']
            house_info["house_type"] = item['houseType']
            try:
                house_info['house_price'] = int(item['price'])
            except Exception as e:
                house_info['price'] = 0
                print e.message
            house_info['addr'] = str(item['addr']).replace(" ", "")

            try:
                house_info["start_time"] = dt.strptime(item["startTime"], "%Y-%m-%d")
            except Exception as e:
                print e.message
                house_info["start_time"] = None

            try:
                house_info["end_time"] = dt.strptime(item["endTime"], "%Y-%m-%d")
            except Exception as e:
                print e.message
                house_info["end_time"] = None

            self.AnjukeItem.insert(house_info)
        return item

    def close_spider(self, spider):
        # self.db.close()
        self.clinet.close()
