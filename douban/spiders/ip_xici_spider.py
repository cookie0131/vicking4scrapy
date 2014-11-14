# -*- coding: utf-8 -*-

from scrapy.spider import Spider
from scrapy.selector import Selector
from scrapy.http.request import Request
from douban.items import ProxyItem
from scrapy import log


class ProxySpider(Spider):
    name = "proxy"
    allowed_domains = ["xici.net.co"]
    start_urls = ['http://www.xici.net.co/']

    def start_requests(self):
        """增加REFER来避免被当成爬虫"""
        requests = []
        for url in self.start_urls:
            requests.append(Request(url, headers={'Referer': 'http://www.baidu.com/s?wd=%E8%A5%BF%E5%88%BA&rsv_spt=1&is'
                                                             'sp=1&f=8&rsv_bp=0&rsv_idx=2&ie=utf-8&tn=baiduhome_pg'}))
        return requests

    def parse(self, response):
        sel = Selector(response)
        infos = sel.xpath('/html/body/div[1]/div[2]/div[1]/div[1]/table/tr')
        items = []
        self.log('>>>>>>>>>>[PROXY] 开始抓取IP信息', level=log.INFO)
        for info in infos:
            item = ProxyItem()
            item['ip'] = info.xpath('td[2]/text()').extract()
            item['port'] = info.xpath('td[3]/text()').extract()
            item['type'] = info.xpath('td[6]/text()').extract()
            items.append(item)
        self.log('>>>>>>>>>>[PROXY] 从页面抓取代理IP，IP信息如下 \t %s' % items, level=log.INFO)
        return items


