#encoding:utf-8 

import urllib2
import re
from bs4 import BeautifulSoup


def get_url_list():
    """计算所有需要爬取的列表页URL"""
    init_url = "http://shanghai.douban.com/events/week-all?start="

    # 需要使用USER-AGENT和Referer，避免被当成爬虫
    request = urllib2.Request(init_url + str(0))
    request.add_header('User-Agent',  'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)')
    request.add_header('Referer', 'http://shanghai.douban.com/')
    response = urllib2.urlopen(request)

    html = response.read()
    soup = BeautifulSoup(html)
    info = soup.findAll(href=re.compile('start='))
    data = info[-3:-2][0].get_text()
    max_id = int(data)*10
    urls = [init_url + str(index) for index in range(0, max_id, 10)]
    return urls