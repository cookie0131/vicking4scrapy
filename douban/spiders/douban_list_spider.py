# -*- coding: utf-8 -*-

from scrapy.spider import Spider
from scrapy.selector import Selector

from douban.items import DoubanItem
from datetime import date
from douban.utils.urls import get_url_list
from scrapy import Request


class DoubanSpider(Spider):
    name = "douban"
    allowed_domains = ["douban.com"]

    # 后续需要用start_request()重写  参考：https://scrapy-chs.readthedocs.org/zh_CN/0.22/topics/spiders.html
    start_urls = get_url_list()
    # start_urls = ['http://shanghai.douban.com/events/week-all?start=0',
    #               'http://shanghai.douban.com/events/week-all?start=10']

    # def start_requests(self):
    #     """增加REFER来避免被当成爬虫"""
    #     requests = []
    #     for item in self.start_urls:
    #         requests.append(Request(url=item, headers={'Referer': 'http://shanghai.douban.com/'}))
    #     return requests

    def parse(self, response):
        sel = Selector(response)
        infos = sel.xpath('/html/body/div[4]/div[1]/div/div[1]/div/ul/li')
        items = []
        time = date.today()
        for info in infos:
            item = DoubanItem()
            url = info.xpath('div[2]/div/a/@href').extract()[0]
            item['act_id'] = url.split('/')[-2]
            item['title'] = info.xpath('div[2]/div/a/span/text()').extract()[0]
            item['start_date'] = info.xpath('div[2]/ul/li[1]/time[1]/@datetime').extract()[0]
            item['end_date'] = info.xpath('div[2]/ul/li[1]/time[2]/@datetime').extract()[0]
            item['event_time'] = info.xpath('div[2]/ul/li[1]/text()').extract()[1].lstrip().rstrip()
            item['address'] = info.xpath('div[2]/ul/li[2]/@title').extract()[0]
            item['cost'] = info.xpath('div[2]/ul/li[3]/strong/text()').extract()[0]
            item['pic'] = info.xpath('div[1]/a/img/@data-lazy').extract()[0]
            item['create_time'] = time
            items.append(item)
        return items
