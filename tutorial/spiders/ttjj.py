# import scrapy
# import sys
# import time
# import os
# from scrapy.selector import Selector
# from scrapy.http import Request
# from lxml import etree 
# sys.path.append('..')
# from tutorial.TtjjItem import TtjjItem
# from scrapy import cmdline
# #循環1到4頁數據
# class Ttjj(scrapy.Spider):
#     name = 'ttjj'
#     start_urls = []
#     url = "http://fund.eastmoney.com/data/rankhandler.aspx?op=ph&dt=kf&ft=all&rs=&gs=0&sc=zzf&st=desc&sd=2018-11-26&ed=2019-11-26&qdii=&tabSubtype=,,,,,&pi=1&pn=50&dx=1&v=0.03528629239491998"
#     start_urls.append(url)
#     def parse(self, response):
#       items = []
      
#       all = response.css('tr')
#       print("======================111")
#       print(all)
#       print("======================222")
#       for ul in all:
#       #   item = TtjjItem()
#       #   item['No'] = ul.xpath('td[2]').get(),
#       #   item['name'] = ul.xpath('td[4]/a/text()').get(),
#       #   item['href'] = ul.xpath('td[4]/a/@href').get(),
#       #   item['code'] = ul.xpath('td[3]/a/text()').get(),
#       #   print("-------------------")
#       #   print(item)
#       #   print("-------------------")
#       #   items.append(item)
#       #   yield item
#             # yield {
              
#                 # 'image': ul.xpath('div[has-class("p_img")]/a/img/@src').get(),
#                 # 'href': ul.xpath('div[has-class("p_productCN")]/a/@href').get(),
#                 # 'name': ul.xpath('div[has-class("p_productCN")]/a/text()').get(),
#                 # 'cost':ul.xpath('div[has-class("p_discount","commonFontPrice")]/text()').getall()
#                 # 'cost': quote.css('span.text::text').get(),
#             # }
#         #怎麼確定下一頁數據存不存在，如果最後一頁不確定呢？？？？
#       for i in range(2, 5):
#         url = "https://www.sephora.cn/hot/?k=%E7%95%85%E9%94%80%E6%A6%9C%E5%8D%95&hasInventory=0&sortField=1&sortMode=desc&currentPage=" + str(i) + "&filters="
#         yield Request(url, callback=self.parse)
    
#     if __name__ == '__main__':
#       while True:
#         os.system("scrapy crawl home2")
#         time.sleep(60)  #每隔一天运行一次 24*60*60=86400s