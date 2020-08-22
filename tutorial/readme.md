1.獲取json文件
scrapy runspider home.py -o home.json -s FEED_EXPORT_ENCODING=UTF-8
2.將爬到的信息存入mysql數據庫，併下載圖片到本地（這裡下載的json文件格式是有問題的）
scrapy crawl home2
3.定時執行時在PS C:\Users\bobo\Desktop\StudyScrapy\tutorial1\tutorial>這個目錄下執行