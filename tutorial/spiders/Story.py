import scrapy
import requests
from fake_useragent import UserAgent
ua=UserAgent()
# from s2.items import S2Item
class Story(scrapy.Spider):
  name = "story"
  # allowed_domains = []
  start_urls = [
    "http://www.quanshuwang.com/list/1_1.html"
  ]
  # for i in range(1,5):
  #   url="http://www.quanshuwang.com/list/1_"+str(i)+".html"
  #   start_urls.append(url)
  #   print(start_urls)

    #获取每一本书的URL
  def parse(self,response):
    headers={"User-Agent":ua.random}
    print("================")
    print(headers)
    print("================")
    response=requests.get(url=url,headers=headers)
    book_urls = response.xpath('//li/a[@class="l mr10"]/@href').extract()
    for book_url in book_urls:
      yield Request(book_url,callback=self.parse_read)
    
    # 获取马上阅读按钮的url，进入章节目录
  def parse_read(self,response):
    read_url = response.xpath('//div[@class="b-oper"]/a[@class="reader"]/@href').extract()
    print(1111111)
    print(read_url)
    print(1111111)
    yield Request(read_url,callback=self.parse_chapter)
    
    # 获取小说章节的URL
  def parse_chapter(self,response):
    chapter_urls = response.xpath('//div[@class="clearfix dirconone"]/li/a/@href').extract()
    for chapter_url in chapter_urls:
      yield Request(chapter_url,callback=self.parse_content)

  def parse_content(self,response):
    bookName = response.xpath('//div[@class="chapName"]/strong/text()').extract()
    author = response.xpath('//div[@class="chapName"]/span[@class="r"]/text()').extract()
    bookUrls = response.xpath('//div[@class="clearfix dirconone"]/li/a/@href').extract()
    chapterName = response.xpath('//div[@class="clearfix dirconone"]/li/a/text()').extract()
    print("================")
    print(response.text)
    print("================")
    for bookUrl in bookUrls:
      yield Request(bookUrl,callback=self.parse_bookContent)

  def parse_bookContent(self,response):
    chapterContent = response.xpath('//div[@class="mainContenr"]/text()')
    item = S2Item()
    item['bookName'] = bookName
    # item['bookUrl'] = self
    item['conetnt'] = chapterContent
    item['author'] = author
    item['chapter'] = chapterName
    yield item
  #  def parse(self, response):
  #     items = []
  #     for res in response.css('ul.seeWell cf'):
  #       item = S2Item()
  #       item['bookHref'] = ul.xpath('li/a[@class="l mr10"]').get(),
  #       item['bookName'] = ul.xpath('li/a[@class="l mr10"]').get(),
  #       item['bookUrl'] = ul.xpath('a/@href').get(),
  #       item['conetnt'] = ul.xpath('a[@class="gs-name text-over-two font14"]/text()').get(),
  #       item['author'] = ul.xpath('span[@class="font14"]/text()').get()
  #       item['chapter'] = ul.xpath('span[@class="font14"]/text()').get()
  #       items.append(item)
  #       yield item
