# -*- coding: utf-8 -*-

# Scrapy settings for ImageCrawling project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'ImageCrawling'

SPIDER_MODULES = ['ImageCrawling.spiders']
NEWSPIDER_MODULE = 'ImageCrawling.spiders'

DEFAULT_ITEM_CLASS = 'ImageCrawling.items.ImageCrawlingItem'
#ITEM_PIPELINES = {'ImageCrawling.pipelines.ImagecrawlingPipeline': 1}
ITEM_PIPELINES = {'ImageCrawling.pipelines.ImagecrawlingPipeline': 1}
IMAGES_STORE = 'C:\Users\Administrator\PycharmProjects\ImageCrawling'


USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ImageCrawling (+http://www.yourdomain.com)'


