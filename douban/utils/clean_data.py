# encoding:utf-8
import MySQLdb
import datetime


def clean_data():
    """清理过期数据"""
    today = str(datetime.date.today())
    conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='douban', port=3306, charset='utf8')
    cur = conn.cursor()
    cur.execute("SELECT * FROM act_info")
    result = cur.fetchall()

    for r in result:
        tmp_end = str(r[3])
        if tmp_end < today:
            # print tmp_end, '<', today, "--->", r[0]
            cur.execute("delete from act_info where act_id = %d" % int(r[0]))
    conn.commit()
    cur.close()
    conn.close()

if __name__ == '__main__':
    clean_data()