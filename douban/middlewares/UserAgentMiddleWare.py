from douban.settings import USER_AGENT_LIST
import random
from scrapy import log


class RandomUserAgentMiddleware(object):

    @staticmethod
    def process_request(request, spider):
        ua = random.choice(USER_AGENT_LIST)
        if ua:
            request.headers.setdefault('User-Agent', ua)
            request.headers.setdefault('Referer', 'http://shanghai.douban.com/')
        # log.msg('>>>>>>>>>>>> UA %s'% request.headers)