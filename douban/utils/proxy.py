# encoding:utf-8
import MySQLdb
import socket


def get_use_proxy():
    """计算可用proxy"""
    conn = MySQLdb.connect(host='localhost', user='root', passwd='', db='douban', port=3306, charset='utf8')
    cur = conn.cursor()
    cur.execute("SELECT * FROM proxy")
    result = cur.fetchall()
    proxy_list = []
    for r in result:
        tmp = check_proxy(r[0], int(r[1]))
        if type(tmp) == dict:
            proxy_list.append(tmp)
    return proxy_list


def check_proxy(ip, port):
    """IP为字符串  PORT为数字"""
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    try:
        s.connect((str(ip), port))
        return {'ip': ip, 'port': port}
    except Exception:
        pass
    s.close()



if __name__ == '__main__':
    get_use_proxy()