# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
import codecs
import pymysql
import base64
import requests
import urllib
import os
import random
import string

import smtplib
import time
import os
from email.mime.text import MIMEText
from email.header import Header
# import MySQLdb
# import MySQLdb.cursors

class TutorialPipeline:
    # def __init__(self):
    #     self.file = codecs.open('douban.json', 'w', encoding='utf-8')
    # def process_item(self, item, spider):
    #     line = json.dumps(dict(item), ensure_ascii=False) + "\n"
    #     self.file.write(line)
    #     return item
    # def spider_closed(self, spider):
    #     self.file.close()


    def __init__(self):
        self.db = None
        self.cursor = None   
    def process_item(self, item, spider):
        #数据库的名字和密码自己知道！！！bole是数据库的名字
        self.db = pymysql.connect(host='localhost', user='root', passwd='123456', db='info')
        self.cursor = self.db.cursor()
        #由于可能报错所以在这重复拿了一下item中的数据，存在了data的字典中
        data = {
            "timer":item['timer'],
            "value":item['value'],
            "bitValue":item['bitValue'],
            "allValue":item['allValue'],
            "tradeValue":item['tradeValue'],
        }
        # imageHref = "http:"+"".join(tuple(data['image']))
        
        # print("=================")
        # print(imageHref)
        # print("=================")
        # os.makedirs('./image/', exist_ok=True)
        # IMAGE_URL = imageHref
        # r = requests.get(IMAGE_URL)
        # ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 18))
        # print(ran_str)
        # imageName = './image/'+ran_str+'.jpg'
        # with open(imageName, 'wb') as f:
        #   f.write(r.content)    

        #注意：MySQL数据库命令语句
        # insert_sql = "INSERT INTO fxh (name, chName, href,value,globalIndex,value24h,number,change,increase) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        print("00000000000000000")
        print(type(data["timer"]))
        insert_sql = "INSERT INTO eos1 ( timer,value, bitValue,allValue,tradeValue) VALUES (%s,%s,%s,%s,%s)"
        try:
            self.cursor.execute(insert_sql, ( data['timer'],data['value'], data['bitValue'], data['allValue'],data['tradeValue']))
            self.db.commit()
        except Exception as e:
            print('问题数据跳过！.......',e)
            self.db.rollback()
       
        self.cursor.close()
        self.db.close()
        return item