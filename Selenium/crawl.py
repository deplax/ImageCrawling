# -*- coding: utf-8 -*-
__author__ = 'Deplax'

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#시간 기록부---------------------------
import time
startTime = int(round(time.time() * 1000))

#한글처리부 ---------------------------
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#main logic--------------------------------------------------

#키워드가 두 단어일 경우 + 추가 필요
keyword = u"아이유"
#url = u"https://www.google.co.kr/imghp"
url = u"https://www.google.co.kr/search?q=" + keyword + u"&tbm=isch"

user_agent = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) " +
    "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.57 Safari/537.36"
)
dcap = dict(DesiredCapabilities.PHANTOMJS)
dcap["phantomjs.page.settings.userAgent"] = user_agent
phantomjsPath = u"/Users/Deplax/project/Crawl/ImageCrawling/Selenium/phantomjs-2.0.0-macosx/bin/phantomjs"
driver = webdriver.PhantomJS(executable_path=phantomjsPath, desired_capabilities=dcap)

driver.get(url)
print driver.current_url
#print driver.page_source
# serchbox = driver.find_element_by_id("gbqfq")
# serchbox.send_keys(keyword, Keys.ENTER)

#timestamp--------------------------
finishTime = int(round(time.time() * 1000))
durationTime = (finishTime - startTime) / 1000.0
print str(durationTime) + " second"