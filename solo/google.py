# -*- coding: utf-8 -*-
__author__ = 'Administrator'

import urllib2
import sys
import os
from scrapy import Selector

print "Google Image Crawling --------------------------------------------------"

#검색 문자열을 받는다.
#중간에 띄어쓰기가 있을 경우 + 처리 필요
keyword = "안녕"
rekeyword = keyword.replace(" ", "+")
keyword = keyword.replace(" ", "_")

#받은 검색 문자열로 html덩어리를 가져온다.
url = "https://www.google.com/search?q=" + rekeyword + "&tbm=isch"
hdr = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36"
request = urllib2.Request(url)
request.add_header("User-agent", user_agent)
contents = urllib2.urlopen(request).read()

#html덩어리에서 이미지 원본 주소만 추출해 리스트로 넣는다.
res = Selector(text=contents)
titleString = u'//div/a/img/@name'
imgString = u'//div[@class="rg_di rg_el"]/a/@href'
title = res.xpath(titleString).extract()
imgurls = res.xpath(imgString).extract()

#저장할 곳을 만든다.
#한글문제 처리
reload(sys)
sys.setdefaultencoding('utf-8')
if not os.path.isdir(keyword):
    os.mkdir(unicode(keyword))

#리스트를 순회하면서 파일을 저장한다.
for i in range(0, len(title) - 1):
    imgurltrim = imgurls[i].split('?imgurl=')[1].split('&imgrefurl=')[0]
    print str(i) + ' : ' + imgurltrim

    try:
        req = urllib2.Request(imgurltrim, headers=hdr)
        imgurl = urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        print e.fp.read()
    except:
        print "??"

    if imgurltrim[-1: -5].find('.') == -1:
        imgurltrim = imgurltrim + ".jpg"
    filename = title[i][0:-1] + '.' + imgurltrim.split('.')[-1]
    if filename.find('/') != -1:
        filename = filename.split('/')[0]
    print filename

    text = imgurl.read()
    if text:
        output = open("./" + keyword + "/" + str(i) + "." + filename, 'wb')
        output.write(text)
        output.close()

    print "crawl finish"

#저장한 갯수와 통계를 보여주고 종료한다.

#javascript setposition
#scroll top