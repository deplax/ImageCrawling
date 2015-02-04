__author__ = 'Administrator'

from scrapy.selector import Selector
from scrapy.http import Request, Response, FormRequest
from scrapy.http import HtmlResponse

#body = '<html><body><span>good</span></body></html>'
#print Selector(text=body).xpath('//span/text()').extract()

print Request(url="http://www.example.com", encoding='utf-8')
print Response(url="http://www.example.com")


response = Request(url="http://www.example.com", method='GET')
print response.body

#print Selector(response=response).xpath('//span/text()').extract()