# -*- coding: utf-8 -*-
from __init__ import  *
import xlwt



#导出数据到file文件夹
def exportTime():
    try:
        sql = "select user.id,user.name,time.time_s,time.date_s,time.content from user left outer join time on user.id = time.id;"
        count = cursor.execute(sql)
        print("查询出" + str(count) + "条记录")
        #来重置游标的位置
        cursor.scroll(0,mode='absolute')
        #搜取所有结果
        results = cursor.fetchall()
        # 获取MYSQL里面的数据字段名称
        fields = cursor.description
        workbook = xlwt.Workbook(encoding = 'utf-8') # workbook是sheet赖以生存的载体。
        sheet = workbook.add_sheet('report',cell_overwrite_ok=True)
        # 写上字段信息
        for field in range(0,len(fields)):
            sheet.write(0,field,fields[field][0])

        for row in range(1,len(results)+1):
            for col in range(0,len(fields)):
                sheet.write(row,col,u'%s'%results[row-1][col])
        #不知道为啥只能用绝对路径，好奇怪
        #workbook.save('/Users/johnny/PycharmProjects2/SM3/file/time.xls')

        # 上传服务器的时候得用这个
        workbook.save('/home/www/SM3/file/time.xls')
        return 1
    except:
        return 0


#导出总的数据到file文件夹
def exportSum():
    try:
        sql = "select A.id,name,A.Sum from (SELECT id,SUM(time_s) as 'Sum' FROM time GROUP BY id) as A left outer join user on A.id = user.id"
        count = cursor.execute(sql)
        print("查询出" + str(count) + "条记录")
        #来重置游标的位置
        cursor.scroll(0,mode='absolute')
        #搜取所有结果
        results = cursor.fetchall()
        # 获取MYSQL里面的数据字段名称
        fields = cursor.description
        workbook = xlwt.Workbook(encoding = 'utf-8') # workbook是sheet赖以生存的载体。
        sheet = workbook.add_sheet('report',cell_overwrite_ok=True)
        # 写上字段信息
        for field in range(0,len(fields)):
            sheet.write(0,field,fields[field][0])

        for row in range(1,len(results)+1):
            for col in range(0,len(fields)):
                sheet.write(row,col,u'%s'%results[row-1][col])
        #不知道为啥只能用绝对路径，好奇怪
        #workbook.save('/Users/johnny/PycharmProjects2/SM3/file/timeSum.xls')

        #上传服务器的时候得用这个
        workbook.save('/home/www/SM3/file/timeSum.xls')
        return 1
    except:
        return 0

