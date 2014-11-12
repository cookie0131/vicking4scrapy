# -*- coding: utf-8 -*-
from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors
from scrapy import log

class DouBanPipeline(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('MySQLdb', db='douban', user='root', passwd='',
                                            cursorclass=MySQLdb.cursors.DictCursor, charset='utf8', use_unicode=True)
        self.act_ids = []

    def process_item(self, item, spider):
        """pipeline默认调用
        不知道为什么，传过来的items在这里被自动拆分成item了"""
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        return item

    def _conditional_insert(self, db, item):
        """把去重过的数据写入数据库"""
        insert_sql = "insert into act_info values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        if item['act_id'] not in self.act_ids:
                db.execute(insert_sql, (item['act_id'], item['title'], item['start_date'], item['end_date'],
                                        item['event_time'], item['address'], item['cost'], item['pic'],
                                        item['create_time']))       # 插入数据库中没有的数据
        else:
            log.msg("%s is in the pool" % item['act_id'], level=log.INFO)

    def open_spider(self, spider):
        """开始前初始化数据，只执行一次"""
        return self.dbpool.runInteraction(self._get_all_act_id)

    def _get_all_act_id(self, db):
        """获取数据库中已经有的act id"""
        get_all_sql = "select act_id from act_info"
        db.execute(get_all_sql)
        tmp_pools = db.fetchall()
        self.act_ids = [t.get('act_id') for t in tmp_pools]    # 获取所有已有数据的id
        return self.act_ids




