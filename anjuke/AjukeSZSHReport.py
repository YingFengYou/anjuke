# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pymongo
import numpy as np
import re
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class AjukeSZSHReport():
    def __init__(self):
        self.clinet = pymongo.MongoClient("localhost", 27017)
        self.db = self.clinet["Anjuke"]
        self.AnjukeItem = self.db["AnjukeInfo"]

    def export_result_piture(self):
        district = [u'曲江', u'城南', u'城东', u'城西', u'周边', u'城北', u'泾渭', u'高新', u'浐灞', u'西咸', u'经济', u'长安']
        x = np.arange(len(district))
        house_price_avg = []
        for district_temp in district:
            results = self.AnjukeItem.find({"addr": re.compile(district_temp)})
            house_price_sum = 0
            house_num = 0
            for result in results:
                house_price_sum += result['house_price']
                house_num += 1
            house_price_avg.append(house_price_sum / house_num)
        bars = plt.bar(x, house_price_avg)
        plt.xticks(x, district)
        plt.rcParams['font.sans-serif'] = ['SimHei']
        i = 0
        for bar in bars:
            plt.text((bar.get_x() + bar.get_width() / 2), bar.get_height(), '%d' % house_price_avg[i], ha='center',
                     va='bottom')
            i += 1
        plt.show()

        def __del__(self):
            self.db.close()


if __name__ == '__main__':
    anjukeSZReport = AjukeSZSHReport()
    anjukeSZReport.export_result_piture()
