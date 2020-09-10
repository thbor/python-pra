

import scrapy
import json
# import nimpy as np
# from np import *
from scrapy.selector import Selector
from scrapy.http import Request
from tutorial.items import TutorialItem
#循環1到4頁數據
class Home(scrapy.Spider):
    name = 'home'
    start_urls = []
    url = "https://dncapi.bqiapp.com/api/coin/web-charts?code=eos&type=all&webp=1"
    start_urls.append(url)
    def parse(self,response):
        jsonBody = json.loads(response.body)
        models = json.loads("["+jsonBody["value"]+"]")
        items = []
        
        for index,model in enumerate(models):
          item = TutorialItem()
          # print("==========")
          # print((model[index]))
          # print("==========")
          item['timer'] = int(model[0])
          item['value'] = model[1]
          item['bitValue'] = model[2] 
          item['allValue'] = model[3]
          item['tradeValue'] = model[4]
          items.append(item)
          yield item
        # for index,model in enumerate(models):
          # print(index)
    # def parse(self, response):
    #     for ul in response.css('div.p_cont'):
    #         yield {
    #             'image': ul.xpath('div[has-class("p_img")]/a/img/@src').get(),
    #             'href': ul.xpath('div[has-class("p_productCN")]/a/@href').get(),
    #             'name': ul.xpath('div[has-class("p_productCN")]/a/text()').get(),
    #             'cost':ul.xpath('div[has-class("p_discount","commonFontPrice")]/text()').getall()
    #             # 'cost': quote.css('span.text::text').get(),
    #         }
    #     #怎麼確定下一頁數據存不存在，如果最後一頁不確定呢？？？？
    #     for i in range(2, 5):  # 爬取第2，4页的数据
    #         url = "https://www.sephora.cn/hot/?k=%E7%95%85%E9%94%80%E6%A6%9C%E5%8D%95&hasInventory=0&sortField=1&sortMode=desc&currentPage=" + str(i) + "&filters="
    #         yield Request(url, callback=self.parse)