# coding=gbk
#
#���ܣ���user�Ǹ�excel����mysql��user��
#
import pymysql
##��ȡexcelʹ��(֧��03)
import xlrd
from builtins import int
from __init__ import conn,cursor

##�����ݿ�
#conn=pymysql.connect(host='localhost',user='root',passwd='ss5122195',db='stuMMMM',port=3306,charset='utf8')
##���α�

cur=cursor

##��excel�ļ�����mysql��
def importExcelToMysql(path):
  workbook=xlrd.open_workbook(path)
  sheets=workbook.sheet_names()
  worksheet=workbook.sheet_by_name(sheets[0])
  #����ǰ��ɾ��
  sql = "delete from user"
  cur.execute(sql)
  ##������
  for i in range(1,worksheet.nrows):
    row=worksheet.row(i)
    
   ##��ʼ������
    sqlstr=[]
    ##������
    for j in range(0,worksheet.ncols):
        ##��������
        sqlstr.append(worksheet.cell_value(i,j))

    ##tb_play_type��
    valuestr=[int(sqlstr[0]),str(int(sqlstr[1])),str(sqlstr[2])]
    print(valuestr)
    try:
        # ִ��SQL���
        #sql = "insert into user(id,password,name) vlaues(5,'5','����')"  # (%s,'%s','%s')" % (int(sqlstr[0]),str(int(sqlstr[1])),str(sqlstr[2]))
        sql = "INSERT INTO user(id,password,name) VALUES(%s,'%s','%s')" % (int(sqlstr[0]),str(int(sqlstr[1])),str(sqlstr[2]))
        cur.execute(sql)
    except:
        print("Error: unable to fetch data")
    ##tb_play_type��

   

  cur.close()
  conn.commit()
  conn.close()
  #��ӡ��Ϣ 
  print("��ϲ�����ݵ���ɹ���")

