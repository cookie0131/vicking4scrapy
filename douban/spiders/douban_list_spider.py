# -*- coding: utf-8 -*-

from scrapy.spider import Spider
from scrapy.selector import Selector

from douban.items import DoubanItem
from datetime import date
from douban.utils.urls import get_url_list


class DouBanSpider(Spider):
    name = "douban"
    allowed_domains = ["douban.com"]
    start_urls = get_url_list()

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
            tmp_start_date = info.xpath('div[2]/ul/li[1]/time[1]/@datetime').extract()[0]
            item['start_date'] = tmp_start_date.split('T')[0]
            tmp_end_date = info.xpath('div[2]/ul/li[1]/time[2]/@datetime').extract()[0]
            item['end_date'] = tmp_end_date.split('T')[0]
            item['time'] = tmp_start_date.split('T')[1] + '-' + tmp_end_date.split('T')[1]
            item['event_time'] = info.xpath('div[2]/ul/li[1]/text()').extract()[1].lstrip().rstrip()
            item['address'] = info.xpath('div[2]/ul/li[2]/@title').extract()[0]
            item['cost'] = info.xpath('div[2]/ul/li[3]/strong/text()').extract()[0]
            item['pic'] = info.xpath('div[1]/a/img/@data-lazy').extract()[0]
            item['create_time'] = time
            items.append(item)
        return items
