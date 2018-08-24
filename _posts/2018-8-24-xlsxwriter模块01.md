--- 
layout: post
title: "Python xlsxwriter系列教程 01"
date: 2018-8-23 16:04:06 
description: "xlsxwriter系列教程"
tag: Python xlsxwriter系列教程
---

# python xlsxwriter 系列教程 01




### xlsxwriter介绍

>XlsxWriter是一个Python模块，用于以Excel 2007+ XLSX文件格式编写文件。

> 它可用于将文本，数字和公式写入多个工作表，它支持格式化，图像，图表，页面设置，自动过滤，条件格式等功能。

### 与其他模块相比

__优点__

- 与其他模块相比有更多丰富的功能

- 高保真，生成的文件可以与Excel生成文件等效

- 官方文档有比较好的示例

- 数度快，大文件输出使用更少的内存

> 官方文档：[https://xlsxwriter.readthedocs.io/getting_started.html#getting-started](
https://xlsxwriter.readthedocs.io/getting_started.html#getting-started)


__缺点__


- 不能对现有Excel文件进行读取和修改




### xlsxwriter 安装

```cython
pip install xlsxwriter
#或者
easy_install XlsxWriter
```

### 使用xlsxwriter 创建一个excel

```cython
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

```

```angular2html
#运行结果
合并区域是： A7:B7
插入计算公式是： =sum(C2:C5)
```

### 效果展示

![展示生成的Excel文件](/images/posts/Python/Xlsxwriter/xlsxwriter_demo.png "展示生成的Excel文件")







推荐阅读：

- [Tkinter Button控件使用-2](https://ssjt21.github.io/2017/11/Python_TK_Button/)

- [Tkinter Entry输入框控件-6](https://ssjt21.github.io/2018/05/Python_TK_Entry/)

- [Python PIL Image类使用](http://ssjt21.github.io/2017/11/Python_PIL_Image_Module/)

- [Python调用Hashcat跑主机密码文件](http://ssjt21.github.io/2017/11/Python_Hashcatshell/)

- [Python pyexcel-xls使用对Excel进行读写操作](https://ssjt21.github.io/2018/1/Python_Pyexcel-xls/)


<br>

转载请注明：[随时静听的博客](http://ssjt21.github.io) » [点击阅读原文](https://ssjt21.github.io/2018/08/xlsxwriter模块01/)


