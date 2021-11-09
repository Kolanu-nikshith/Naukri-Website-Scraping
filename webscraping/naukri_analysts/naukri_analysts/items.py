# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobItem(scrapy.Item):
    job_title=scrapy.Field()
    experience=scrapy.Field()
    location=scrapy.Field()
    company_name=scrapy.Field()
    keyskills=scrapy.Field()
    link=scrapy.Field()
    job_description=scrapy.Field()
    salary=scrapy.Field()
   