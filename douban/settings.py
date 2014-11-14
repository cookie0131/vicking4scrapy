# -*- coding: utf-8 -*-

# Scrapy settings for douban project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'douban'

SPIDER_MODULES = ['douban.spiders']
NEWSPIDER_MODULE = 'douban.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'douban (+http://www.yourdomain.com)'

# 调用Pipelines的开关
ITEM_PIPELINES = {'douban.douban_pipelines.DouBanPipeline': 100,
                  'douban.proxy_pipelines.ProxyPipeline': 10}

#日志级别 CRITICAL、 ERROR、WARNING、INFO、DEBUG
LOG_LEVEL = 'ERROR'

# 错误页面重试机制
RETRY_ENABLED = True
RETRY_TIMES = 3
RETRY_HTTP_CODES = [500, 502, 503, 504, 400, 408]

COOKIES_ENABLED = False
DOWNLOAD_DELAY = 2.5
RANDOMIZE_DOWNLOAD_DELAY = True
DOWNLOAD_TIMEOUT = 30


USER_AGENT_LIST = ['Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.54 Safari/536.5',
                   'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.124 Safari/537.36',
                   'Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0',
                   'Mozilla/5.0 (Windows; U; Windows NT 5.1) Gecko/20070309 Firefox/2.0.0.3',
                   'Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1',
                   'Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30',
                   'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
                   ]

DOWNLOADER_MIDDLEWARES = {
    # 'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
    'douban.middlewares.ProxyMiddleWare.ProxyMiddleware': 200,
    # 中间件将重试临时的问题    RETRY_ENABLED  RETRY_TIMES  RETRY_HTTP_CODES
    'douban.middlewares.RetryMiddleWare.RetryMiddlewareSubclass': 300,
    'douban.middlewares.UserAgentMiddleWare.RandomUserAgentMiddleware': 400,
    'scrapy.contrib.downloadermiddleware.useragent.UserAgentMiddleware': None,
}
