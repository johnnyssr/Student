from __init__ import cursor,conn
import datetime

def execuesql(sql):
    # 执行SQL，并返回收影响行数
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchone()
        # 返回结果
        return results[0]
    except:
        print("Error: unable to fetch data")

def select_password_sql(user_id):
    # #创建连接
    # conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='ss5122195', db='weiboDB')
    # # 创建游标
    # cursor = conn.cursor()

    # SQL 查询语句
    sql = "SELECT password FROM user WHERE id = %s"%user_id

    return execuesql(sql)

    # # 提交，不然无法保存新建或者修改的数据
    # conn.commit()
    # #关闭游标
    #cursor.close()
    # #关闭连接
    #conn.close()

#查询用户的名字
def select_name_sql(user_id):
    # SQL 查询语句
    sql = "SELECT NAME FROM user WHERE id = %s" % user_id

    return execuesql(sql)

def insert_time_sql(id,time,date,content):
    dt = datetime.datetime.now().strftime("%Y-%m-%d")
    dt = '2012-12-12'
    sql = "INSERT INTO time (id,time_s,date_s,content) VALUES(%s,%s,'%s','%s')" %(id,time,date,content)

    try:
        # 执行SQL语句
        cursor.execute(sql)
        conn.commit()
        return 1
    except:
        print("Error: unable to fetch data")
        return 0

def select_time_sql(user_id):
    # SQL 查询语句
    sql = "SELECT time_s,date_s,content FROM time WHERE id = %s" % user_id

    # 执行SQL，并返回收影响行数
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        #返回结果
        return results
    except:
        print("Error: unable to fetch data")



def select_all_sql():
    # SQL 查询语句
    sql = "select user.id,user.name,time.time_s,time.date_s,time.content from user left outer join time on user.id = time.id;"
    # 执行SQL，并返回收影响行数
    try:
        # 执行SQL语句
        cursor.execute(sql)
        # 获取所有记录列表
        results = cursor.fetchall()
        #返回结果
        # for i in results:
        #     print(i)
        return results
    except:
        print("Error: unable to fetch data")