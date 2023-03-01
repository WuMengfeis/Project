# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
from twisted.enterprise import adbapi
from pymysql import cursors

class ZhaopinTwistedPipeline(object):
    def __init__(self):
        dbparams = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'password': '123456',
            'database': 'zhaopin',
            'charset': 'utf8',
            'cursorclass':cursors.DictCursor
        }
        self.dbpool = adbapi.ConnectionPool('pymysql',**dbparams)
        self.job_sql = """
                        insert into job (id,number,job,post_type,city,job_place,job_experience,education,min_wage,max_wage,job_duty,job_benefits,update_time) values (null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    """
        self.company_sql = """
                        insert into company (number,company,logo,website,industry,scale) values (%s,%s,%s,%s,%s,%s)
        """

    # @property
    # def sql(self):
    #     if not self._sql:
    #         self._sql = """
    #             insert into data (id,url,job,job_category,salary,company,working_place,experience,educational,job_keys,job_description) values (null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
    #         """
    #         return self._sql
    #     return self._sql

    def process_item(self, item, spider):
        defer = self.dbpool.runInteraction(self.insert_item,item)
        defer.addErrback(self.handle_error,item,spider)
        return item

    def insert_item(self,cursor,item):
        print("插入数据")
        cursor.execute(self.job_sql,(item['number'],item['job'],item['post_type'],item['city'],item['job_place'],
                                     item['job_experience'],item['education'],item['min_wage'],item['max_wage'],
                                     item['job_duty'],item['job_benefits'],item['update_time'] ))
        cursor.execute(self.company_sql, (item['number'], item['company'], item['logo'], item['website'],
                                          item['industry'],item['scale']))

    def handle_error(self,error,item,spider):
        print('='*10+'error'+'='*10)
        print(item)
        print(error)
        print('='*10+'error'+'='*10)


# ip代理池实现方法
# from scrapy import signals
# from twisted.internet.defer import DeferredLock
# from .settings import USER_AGENT_LIST,DEFAULT_REQUEST_HEADERS
# import random
# import requests
# import json
# from .model import ProxyModel
#
#
# class BossDownloaderMiddleware(object):
#     def __init__(self):
#         self.current_proxy = None
#         self.lock = DeferredLock()
#
#     def process_request(self, request, spider):
#         user_agent = random.choice(USER_AGENT_LIST)
#         request.headers['User-Agent'] = user_agent
#
#         #如果没有使用代理或者代理即将过期
#         if 'proxy' not in request.meta or self.current_proxy.is_expiring:
#             self.update_proxy()
#             request.meta['proxy'] = self.current_proxy
#
#
#     def process_response(self, request, response, spider):
#         #如果被重定向到403或者要求识别验证码
#         if response.status !=200 or 'captcha' in response.url:
#             #如果被要求识别验证码，则我们让response理解为ip别封了
#             if not self.current_proxy.blacked:
#                self.current_proxy.blacked = True
#             self.update_proxy()
#             request.meta['proxy'] = self.current_proxy
#             return request
#         return response
#
#     def update_proxy(self):
#         # lock是属于多线程中的一个概念，因为这里scrapy是采用异步的，可以直接看成多线程
#         # 所以有可能出现这样的情况，爬虫在爬取一个网页的时候，忽然被对方封了，这时候就会来到这里
#         # 获取新的IP，但是同时会有多条线程来这里请求，那么就会出现浪费代理IP的请求，所以这这里加上了锁
#         # 锁的作用是在同一时间段，所有线程只能有一条线程可以访问锁内的代码，这个时候一条线程获得新的代理IP
#         # 而这个代理IP是可以用在所有线程的，这样子别的线程就可以继续运行了，减少了代理IP（钱）的浪费
#         self.lock.acquire()
#         # 判断换线程的条件
#         # 1.目前没有使用代理IP
#         # 2.到线程过期的时间了
#         # 3.目前IP已经被对方封了
#         # 满足以上其中一种情况就可以换代理IP了
#         if not self.current_proxy or self.current_proxy.is_expiring or self.current_proxy.blacked:
#             url = r'https://h.wandouip.com/get/ip-list?pack=%s&num=1&xy=1&type=2&lb=\r\n&mr=1&' % random.randint(100,1000)
#             response = requests.get(url,headers=DEFAULT_REQUEST_HEADERS)
#             text = json.loads(response.text)
#             print(text)
#             data = text['data'][0]
#             proxy_model = ProxyModel(data)
#             self.current_proxy = proxy_model
#
#         self.lock.release()
