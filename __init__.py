import pymysql

#创建连接,加上charset=utf8保证能识别中文
conn = pymysql.connect(host='47.94.98.6', port=3306, user='root', passwd='ss5122195', db='stuMMMM',charset='utf8')
# 创建游标
cursor = conn.cursor()

