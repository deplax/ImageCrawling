# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.contrib.pipeline.images import ImagesPipeline
from scrapy.exceptions import DropItem
from PIL import Image
import scrapy

class ImagecrawlingPipeline(object):

    # def __init__(self):
		# self.file = codecs.open("items.json", "wb", encoding="utf-8")



    def get_media_requests(self, item, info):
        for image_url in item['image_url']:
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_url'] = image_paths
        return item

    def process_item(self, item, spider):
        # line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        # self.file.write(line)
        return item