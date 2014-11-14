# -*- coding: utf-8 -*-
from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors


class ProxyPipeline(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('MySQLdb', db='douban', user='root', passwd='',
                                            cursorclass=MySQLdb.cursors.DictCursor, charset='utf8', use_unicode=True)
        self.ips = []

    def process_item(self, item, spider):
        """pipeline默认调用
        不知道为什么，传过来的items在这里被自动拆分成item了"""
        if spider.name == 'proxy':
            query = self.dbpool.runInteraction(self._conditional_insert, item)
        return item

    def _conditional_insert(self, db, item):
        """把去重过的数据写入数据库"""
        insert_sql = "insert into proxy values (%s,%s,%s)"

        if len(item['ip']) > 0 and item['type'][0] == 'HTTP' and item['ip'][0] not in self.ips:
            # log.msg("---------> %s,%s" % (item['ip'], item['port']), level=log.INFO)
            db.execute(insert_sql, (item['ip'], item['port'], item['type']))

    def open_spider(self, spider):
        """开始前初始化数据，只执行一次"""
        return self.dbpool.runInteraction(self._get_all_proxys)

    def _get_all_proxys(self, db):
        """获取数据库中已经有的act id"""
        db.execute("select ip from proxy")
        tmp_ips = db.fetchall()
        self.ips = [t.get('ip') for t in tmp_ips]    # 获取DB中所有IP
        return self.ips

