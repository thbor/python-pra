

# import scrapy
# import json
# import sys
# import requests
# import time
# import os
# from scrapy.selector import Selector
# from scrapy.http import Request
# sys.path.append('..')

# sys.path.append(r'C:\Users\bobo\Desktop\StudyScrapy\tutorial\tutorial\items.py')
# from tutorial.items import TutorialItem

# from scrapy import cmdline
import scrapy
import json
import sys
import time
import os
from scrapy.selector import Selector
from scrapy.http import Request
sys.path.append('..')
from tutorial.items import TutorialItem
from scrapy import cmdline
#循環1到4頁數據
class Eos1(scrapy.Spider):
    name = 'eos1'
    start_urls = []
    url = "https://dncapi.bqiapp.com/api/coin/web-charts?code=eos&type=all&webp=1"
    start_urls.append(url)
    def parse(self,response):
        jsonBody = json.loads(response.body)
        models = json.loads("["+jsonBody["value"]+"]")
        items = []
        
        for index,model in enumerate(models):
          item = TutorialItem()
          item['timer'] = int(model[0])
          item['value'] = model[1]
          item['bitValue'] = model[2] 
          item['allValue'] = model[3]
          item['tradeValue'] = model[4]
          items.append(item)
          yield item
    if __name__ == '__main__':
      while True:
        os.system("scrapy crawl eos1")
        time.sleep(60)