# -*- coding: utf-8 -*-

from scrapy.contrib.downloadermiddleware.retry import RetryMiddleware
from scrapy import log


class RetryMiddlewareSubclass(RetryMiddleware):

    def process_response(self, request, response, spider):
        response = RetryMiddleware.process_response(self, request, response, spider)

        if response.status in [500, 503, 504, 400, 403, 404, 408]:
            print '>>>>>>>> HTTP ERROR retry Requesting url %s with proxy %s...' % (request.url, request.meta['proxy'])
            return self._retry(request, 'retry for http error', spider) or response
        else:
            return response