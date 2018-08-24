# -*- coding: utf-8 -*-

"""
@author:随时静听
@file: 创建.py
@time: 2018/08/24
@email:wang_di@topsec.com.cn
"""

#导入xlsxwriter 用于创建xlsx

import xlsxwriter


#创建 一个Workbook 实列
book=xlsxwriter.Workbook(u'员工.xlsx')

#添加一个工作簿
sheet=book.add_worksheet()
#可以指定工作的名字也可以不指定，如果需要指定，按照下面的写法加入参数即可
#再次添加一个名字为 '员工表'工作簿
sheet2=book.add_worksheet(u'员工表')

#写入数据

# 第一个工作簿写入数据

sheet.write("A2",u"序号")#A2单元格写入 序号
#这里的字母A必须大写
sheet.write(1,1,u"姓名") # 第二行 第二列 写入 姓名
sheet.write(1,2,u"报销费用")

#使用循环写数据

expenses = (
    ['Rent', 1000],
    ['Gas',   100],
    ['Food',  300],
    ['Gym',    50],
)

row=2
col=0

for index,item in enumerate(expenses):
    sheet.write(row,col,index+1)#写入序号值
    sheet.write(row,col+1,item[0])#写入姓名
    sheet.write(row,col+2,item[1]) # 报销费用
    row+=1

#合并单元格 写入内容
merge_range='A'+str(row+1)+':B'+str(row+1) #合并单元格的范围，一般都是"A2:B2","A2:D4"这样的格式
print "合并区域是：" ,merge_range
sheet.merge_range(merge_range,u'合计：')

#写入公式
Calculation_formula='=sum(C3:C'+str(row-1)+")"
print "插入计算公式是：", Calculation_formula
sheet.write(row,2,Calculation_formula)

book.close()#关闭




if __name__ == '__main__':
    pass