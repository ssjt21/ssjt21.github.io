---
layout: post
title: "Python 天融信报告HTML转Excel"
date: 2017-11-15 13:13:06 
description: "解决报告中繁琐的复制粘贴工作，将报告中的表格保存到Excel中"
tag: Python
---


解决报告中繁琐的复制粘贴工作，将报告中HTML中的各个等级的漏洞信息给写入到Excel中，方便后期的一次性的统计结果。

### Python 脚本实现
``` Python
# -*- coding: utf-8 -*-
import re
import os
import glob
from xlrd import open_workbook
from xlutils.copy import copy
import time

# 获取当前文件夹下的所有合规的文文件夹
def  GetDir(path=''):
    #第一次筛选
    dirlst= glob.glob('2017*')
    # 第二次筛选
    dirlst= [dir for dir in dirlst  if re.match('\d{12,14}',dir) ]
    # 拼接路径
    dirlst=[ os.path.join(os.getcwd(),path,'detail') for path in dirlst ]
    return dirlst

# 获取指定路径下所有HTML文件
def GetFilePath(DirPath):
    if DirPath:
        filePath= os.listdir(DirPath) #glob.glob(DirPath+"\\*")
        filePath= [ os.path.join(DirPath,file) for file in filePath if re.match('\d{3,30}\.html',file) ]
        return filePath
    else:
        return []

#读取html文件中的内容
def ReadHtml(filePath):
    file=open(filePath,'r')
    content=file.read()
    file.close()
    return content

# 获取漏洞名 4.描述 5. 解决方案 6.危险等级
def GetData(content):
    pattern=re.compile('<tr>([\s\S]*?)</tr>')
    match=pattern.findall(content)
    # 3. 漏洞名 4.描述 5. 解决方案 6.危险等级  15主机
    match= [ re.findall('<td[\s\S]*?>([\s\S]*?)</td>',item)[1] for item in  (match[2:6]+[match[-1]]) ]
    if(match[3]=="信息"):
        return False
    else:
        return match
# 获取指定等级的data
def GetLevel(Datalist,level):#这个函数可以优化
    datalst=[]
    for line in   Datalist:
        if line[3]==level:
            tmp=[]#     修改每条数据的顺序
            tmp.append(line[0])
            tmp.append(line[3])
            tmp.append(line[-1])
            tmp.append(line[1])
            tmp.append(line[2])
            datalst.append(tmp)
    return datalst
# 将数据写入Excel
def WriteExcel(Datalist,path): 
    rb=open_workbook('./test.xlsx')
    wb=copy(rb)
    for row , line in enumerate(Datalist):
        #写入序号
        wb.get_sheet(0).write(row+1,0,str(row+1).decode('utf-8'))
        for col , item in enumerate(line):#写入每条一行
            wb.get_sheet(0).write(row+1,col+1,str(item).decode('utf-8'))
    excel_name=time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime())+'.xls'
    wb.save(os.path.join(os.path.split(path)[0],excel_name))
    print excel_name,"保存成功,路径位置：",os.path.join(os.getcwd(),excel_name)
#运行函数
def Run():
    detail_dir=GetDir()
    for dir in detail_dir:
        html_List=GetFilePath(dir)
        result_list=[]
        for html in html_List:
            html_content=ReadHtml(html)
            data=GetData(html_content)
            if data:
                result_list.append(data)
        urgent_level_list=GetLevel(result_list,"紧急")       
        hig_level_list=GetLevel(result_list,"高级") 
        medium_level_list=GetLevel(result_list,"中级") 
        low_level_list=GetLevel(result_list,"低级") 
        result=urgent_level_list+hig_level_list+hig_level_list+medium_level_list+low_level_list
        WriteExcel(result,dir)

if __name__=="__main__":
    Run()
```

### 使用说明

- 依赖库 xlrd、 xlutils

- 需要模板test.xlsx 模板中可以无任何内容（脚本同级目录）

- 报告解压出的文件名为原始文件名，不要动原始解压文件的名字

- 可进行批量文件的处理，无需传递任何参数，运行脚本即可完成所有操作

- 提供.exe可执行程序无需进行任何依赖包的安装

- [报告HTML转Excel(.exe下载)](http://pan.baidu.com/s/1bpIuES3) 密码 **2vuk**



推荐阅读：

- [Python调用Hashcat跑主机密码文件](http://ssjt21.github.io/2017/11/Python_Hashcatshell/)

- [Python 绿盟HTML报告转Excel](http://ssjt21.github.io/2017/11/Python_NSFOCUS_To_Excel/)

- [Excel VLOOKUP函数](http://ssjt21.github.io/2017/11/Excel_vlookup/)

- [Excel 根据表格内容修改格式](http://ssjt21.github.io/2017/11/Excel_ConditionFormat/)


<br>

转载请注明：[随时静听的博客](http://ssjt21.github.io) » [点击阅读原文](http://ssjt21.github.io/2017/11/Python_HtmltoExcel/)