# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class NullFixPipeline(object):
    def process_item(self, item, spider):
        try:
        	item['job_description']
        except KeyError:
        	item['job_description']='Available in Link'
        
        try:
        	item['keyskills']
        except KeyError:
        	item['keyskills']='Available in Link'




        return item
