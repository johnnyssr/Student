# coding=gbk
#
#功能：将user那个excel导入mysql的user表
#
import pymysql
##读取excel使用(支持03)
import xlrd
from builtins import int
from __init__ import conn,cursor

##打开数据库
#conn=pymysql.connect(host='localhost',user='root',passwd='ss5122195',db='stuMMMM',port=3306,charset='utf8')
##打开游标

cur=cursor

##将excel文件导入mysql中
def importExcelToMysql(path):
  workbook=xlrd.open_workbook(path)
  sheets=workbook.sheet_names()
  worksheet=workbook.sheet_by_name(sheets[0])
  #把以前的删了
  sql = "delete from user"
  cur.execute(sql)
  ##遍历行
  for i in range(1,worksheet.nrows):
    row=worksheet.row(i)
    
   ##初始化数组
    sqlstr=[]
    ##遍历列
    for j in range(0,worksheet.ncols):
        ##构造数组
        sqlstr.append(worksheet.cell_value(i,j))

    ##tb_play_type表
    valuestr=[int(sqlstr[0]),str(int(sqlstr[1])),str(sqlstr[2])]
    print(valuestr)
    try:
        # 执行SQL语句
        #sql = "insert into user(id,password,name) vlaues(5,'5','好人')"  # (%s,'%s','%s')" % (int(sqlstr[0]),str(int(sqlstr[1])),str(sqlstr[2]))
        sql = "INSERT INTO user(id,password,name) VALUES(%s,'%s','%s')" % (int(sqlstr[0]),str(int(sqlstr[1])),str(sqlstr[2]))
        cur.execute(sql)
    except:
        print("Error: unable to fetch data")
    ##tb_play_type表

   

  cur.close()
  conn.commit()
  conn.close()
  #打印信息 
  print("恭喜，数据导入成功！")

