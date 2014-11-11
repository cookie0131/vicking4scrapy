# -*- coding: utf-8 -*-
from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors

from scrapy import log
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DoubanPipeline(object):
    def __init__(self):
        self.dbpool = adbapi.ConnectionPool('MySQLdb', db='douban', user='root', passwd='',
                                            cursorclass=MySQLdb.cursors.DictCursor, charset='utf8', use_unicode=True)
        
    def process_item(self, item, spider):
        """pipeline默认调用
        不知道为什么，传过来的items在这里被自动拆分成item了"""
        print "############################################BEGIN###############################################"
        query = self.dbpool.runInteraction(self._conditional_insert, item)
        print "############################################END###############################################"
        return item

    def _conditional_insert(self, db, item):
        """把去重过的数据写入数据库"""
        get_all_sql = "select act_id from act_info"
        insert_sql = "insert into act_info values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        # db.execute(get_all_sql)
        # tmp_pools = db.fetchall()
        # pools = [t.get('act_id') for t in tmp_pools]    # 获取所有已有数据的id
        if item['act_id'] not in pools:
                db.execute(insert_sql, (item['act_id'], item['title'], item['start_date'], item['end_date'],
                                        item['event_time'], item['address'], item['cost'], item['pic'],
                                        item['create_time']))       # 插入数据库中没有的数据
        else:
            log.msg("%s is not in the pool" % item['act_id'], level=log.INFO)

