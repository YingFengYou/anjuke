# -*- coding: utf-8 -*-
import json
import telnetlib
import requests
import random
import pymongo

class proxyTool(object):

    def __init__(self):
        self.proxy_url = 'https://raw.githubusercontent.com/fate0/proxylist/master/proxy.list'
        self.clent = pymongo.MongoClient("localhost", 27017)
        self.db = self.clent['Anjuke']
        self.proxys = self.db['proxys']

    def verify(self, ip, port, type):
        proxies = {}
        try:
            telnet = telnetlib.Telnet(ip, port=port, timeout=3)
        except:
            print('unconnected')
        else:
            # print('connected successfully')
            # proxyList.append((ip + ':' + str(port),type))
            proxies['type'] = type
            proxies['host'] = ip
            proxies['port'] = port
            self.proxys.insert(proxies)
            # proxiesJson = json.dumps(proxies)
            # with open('verified_proxies.json', 'a+') as f:
            #     f.write(proxiesJson + '\n')
            # print("已写入：%s" % proxies)

    def getProxy(self, ):
        response = requests.get(self.proxy_url)
        proxies_list = response.text.split('\n')
        for proxy_str in proxies_list:
            proxy_json = json.loads(proxy_str)
            host = proxy_json['host']
            port = proxy_json['port']
            type = proxy_json['type']
            self.verify(host, port, type)


tool = proxyTool()
tool.getProxy()
