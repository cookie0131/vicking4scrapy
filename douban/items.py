# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy.item


class DoubanItem(scrapy.Item):
    """抓取豆瓣的页面的数据模型"""
    act_id = scrapy.Field()
    title = scrapy.Field()
    start_date = scrapy.Field()
    end_date = scrapy.Field()
    event_time = scrapy.Field()
    address = scrapy.Field()
    cost = scrapy.Field()
    pic = scrapy.Field()
    create_time = scrapy.Field()


class ProxyItem(scrapy.Item):
    """IP代理的模型"""
    ip = scrapy.Field()
    port = scrapy.Field()
    type = scrapy.Field()
    status = scrapy.Field()
