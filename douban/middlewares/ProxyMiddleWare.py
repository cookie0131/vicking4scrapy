import random
from douban.utils.proxy import get_use_proxy
from scrapy import log


# Start your middleware class
class ProxyMiddleware(object):

    def __init__(self):
        self.proxy_list = get_use_proxy()

    def process_request(self, request, spider):
        #ip_list = get_use_proxy()
        ip_list = self.proxy_list
        index = random.randint(0, len(ip_list)-1)
        request.meta['proxy'] = 'http://%s:%s' % (ip_list[index]['ip'], ip_list[index]['port'])
        # log.msg('>>>>>>>>>>>> Proxy %s' % request.meta['proxy'])
        # print '>>>>>>>>>>>> Proxy %s Request %s' % (request.meta['proxy'], request.url)