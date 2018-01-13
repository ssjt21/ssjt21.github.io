--- 
layout: post
title: "Python pyexcel-xls使用"
date: 2018-1-4 14:25:06 
description: "Python pyexcel-xls使用,对excel的读写操作"
tag: Python
---

pyexcel-xls是一个比较小的xls操作模块，支持xls格式读取和写入操作，但是对于 xlsx和 xlsm格式只能进行读取不能进行写入操作。

### 限制性

- 不支持 字体、颜色、图表的操作
- 只对 xls 格式有读写两种操作
- 对xlsx和 xlsm只有读操作
- 对于限制性你可以使用pyexcel-xlsx模块对(.xlsx)操作
- 详细的格式支持参考信息[pyexcel 官方](http://pythonhosted.org/pyexcel/)

### 安装

```PYTHON
pip install pyexcel-xls
pip install pyexcel-xlsx
```

### 优势

- 读取的数据是个有序字典(OrderedDict)
- 以sheet名作为字典的key
- value是sheet表中数据,类型为列表(list),包含的数据也是list,并以行的形式存储

### 向 excel(.xls)文件写入数据

- save_data(filename,OrderedDict\_data) 数据写入文件
- filename 是写入的文件名
- OrderedDict\_data是写入的数据,类型是有序字典(OrderedDict)

```python
# -*- coding: utf-8 -*-
from pyexcel_xls import save_data
from collections import OrderedDict

def write_xls_file(filename="./test.xls"):
    data=OrderedDict()
    sheet_1=[]
    sheet_2=[]
    row_data_1=["ID",u"姓名",u"成绩"]
    row_data_2=[1,u"小明",88]
    sheet_1.append(row_data_1)
    sheet_2.append(row_data_2)
    data.update({"first_sheet":sheet_1})
    data.update({"second_sheet":sheet_2})
    save_data(filename,data)
if __name__=="__main__":
    write_xls_file()
```

### 读excel (.xls|.xlsx|.xlsm)文件的数据

- get_data(filename),读取文件filename中的数据
- 返回的结果是一个有序字典(OrderedDict)

```python
# -*- coding: utf-8 -*-
from collections import OrderedDict
from pyexcel_xls import get_data

def read_from_xls(filename="./test.xls"):
    data=get_data(filename)
    print type(data)
    for key,value in data.items():
        print key,value
if __name__=="__main__":
    read_from_xls()
#结果：
<class 'collections.OrderedDict'>
first_sheet [[u'ID', u'\u59d3\u540d', u'\u6210\u7ee9']]
second_sheet [[1, u'\u5c0f\u660e', 88]]
```

### 除以上操作外，还支持对IO操作，比如文件的上传和下载

- 文件的保存使用sava_data()
- 文件的的读取使用get_data()
- 操作的对象由文件名变成 StingIO()创建的对象

### pyexcel.ext 插件使用 

```Python
# -*- coding: utf-8 -*-
import pyexcel as pe
from pyexcel.ext import xls
#读取数据
sheet=pe.get_book(file_name="./test.xls")
print sheet
#写入数据
sheet.save_as("test3.xls")
#结果：
first_sheet:
+----+------+------+
| ID | 姓名 | 成绩 |
+----+------+------+
second_sheet:
+---+------+----+
| 1 | 小明 | 88 |
+---+------+----+
```
[pyexcel-xls 官方文档](http://pythonhosted.org/pyexcel-xls/)

***

> pyexcel-xlsx使用方法和pyexcel-xls一样


推荐阅读：

- [Tkinter Button控件使用-2](https://ssjt21.github.io/2017/11/Python_TK_Button/)


- [Python PIL Image类使用](http://ssjt21.github.io/2017/11/Python_PIL_Image_Module/)

- [Python调用Hashcat跑主机密码文件](http://ssjt21.github.io/2017/11/Python_Hashcatshell/)

- [Python Nmap批量主机存活检测脚本](https://ssjt21.github.io/2018/1/Python_Nmap批量主机存活检测/)

<br>

转载请注明：[随时静听的博客](http://ssjt21.github.io) » [点击阅读原文](https://ssjt21.github.io/2018/1/Python_Pyexcel-xls/)

