# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import scrapy
from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem


class MeitulePipeline(ImagesPipeline):

    """
    def process_item(self, item, spider):
        print '>>>>>>>>>> process_item <<<<<<<<<<<<<<'
        return item
    """

    def get_media_requests(self, item, info):
        print '>>>>>>>>>> get_media_requests <<<<<<<<<<<<<<'
        for image_url in item['image_urls']:
            _idx = image_url.rfind('/')
            if _idx>0:
                _title = image_url[_idx:]
            else:
                _title = image_url
            print '>>>>>>>>>> get_media_requests.url=<%s>,title=<%s> <<<<<<<<<<<<<<' % (image_url,_title)
            yield scrapy.Request(image_url,meta={'name':'viewport','content':'width=device-width,minimum-scale=0.1'})

    def item_completed(self, results, item, info):
        print '>>>>>>>>>> item_completed <<<<<<<<<<<<<<'
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item

