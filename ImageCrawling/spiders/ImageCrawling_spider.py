# -*- coding: utf-8 -*-
__author__ = 'Administrator'
import scrapy
from scrapy.selector import Selector
from ImageCrawling.items import ImagecrawlingItem

class ImageCrawlingSpider(scrapy.Spider):
    name = "ImageCrawling"
    allowed_domains = ["https://www.google.com/"]

    #먼저 크롤링할 URL을 세팅한다.
    start_urls = [
        "https://www.google.com/search?q=keep&tbm=isch"
    ]

    #scrapy에서는 자동으로 url이 request되어 결과가 response인자로 들어와 parse가 실행된다.
    def parse(self, response):
        self.log('A response from %s just arrived!' % response.url)

        print '--------------------------------------------------------------------------------------'
        #Selector위치 지정
        res = Selector(response)
        titleString = u'//div/a/img/@name'
        imgString = u'//div[@class="rg_di rg_el"]/a/@href'
        title = res.xpath(titleString).extract()
        img = res.xpath(imgString).extract()

        #item.py에 있는 클래스를 불러온다.
        item = ImagecrawlingItem()

        #차곡차곡
        for i in range(0, len(title) - 1):
            item['title'] = title[i]
            item['image_url'] = img[i].split('?imgurl=')[1].split('&imgrefurl=')[0]
            yield item

        print '--------------------------------------------------------------------------------------'

        # filename = response.url.split(".")[-2]
        # with open(filename, 'wb') as f:
        #     f.write(response.body)