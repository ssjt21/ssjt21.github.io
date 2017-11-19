---
layout: post
title: "Python 绿盟HTML报告转Excel"
date: 2017-11-19 10:13:06 
description: "山东中移在线需要对绿盟的报告进行处理成指定的格式"
tag: Python
---

之前对数据的处理都是直接使用正则，使用正则虽然繁琐，但是写出的东西速度是很快的，使用BeautifulSoup模块固然很快，但也是有很多的问题，比如当读入的数据很多很大的时候就崩溃掉，不得一步移步将其剥离，直到找到更小的范围后再进行处理。本篇中写没有使用正则的原因是，发现绿盟的报告用正则匹配能让人疯掉的感觉。再实现的过程中，需要不断的调试确定你获得的是什么样的对象，再则就是你拿到的数据怎么处理和编码在写入到Excel中。整个代码花了将近一天的时间，基本上都是，处理获得目标内容和编码问题。这里说的是BeautifulSoup中`bs4.element.NavigableString`转码问题，最后通过查看文档解决。

[BeautifulSoup 中文文档](https://www.crummy.com/software/BeautifulSoup/bs4/doc/index.zh.html)

[Python xlsxwriter 官方文档](https://xlsxwriter.readthedocs.io/)

### Python 实现代码 --学了不少东西(is in 区别)
```Python
# -*- coding: utf-8 -*-
import re
import time
import os
import xlsxwriter
import glob
import bs4
from bs4 import BeautifulSoup

# 获取说有HTML路径
def Get_Html_PAHT_list(path=os.getcwd()):
    Html_Path_List=[]
    if path:
        Html_Path_List=glob.glob("index.html")
    else:
        print u"the parameter must be a path"
        pass
    return Html_Path_List
    
# 读取HTML中的内容
def ReadHtml(filePath):
    file=open(filePath,'r')
    content=file.read()
    file.close()
    return content

#获得目标tag标签的内容
def get_dst_tag(n,dst_tag):
    for x,tag in enumerate(dst_tag):
        if x==n:
            return tag
# 获取数据并写入Ecel
def Get_Data(content):
    soup=BeautifulSoup(content,"lxml")
    # 9 12 2 (1,3) 3（tbody）此项参数是通过调试输出获得的
    # (1,3)1是统计漏洞数量，3是目标数据的详细情况
    dst_tag=soup.body.div.children
    dst_tag=get_dst_tag(9,dst_tag)
    dst_tag=get_dst_tag(12,dst_tag)
    dst_tag=get_dst_tag(2,dst_tag)
    dst_tag=get_dst_tag(3,dst_tag)
    dst_tag=get_dst_tag(3,dst_tag)
    i=0 #通过这个变量可以将标签分组(单--漏洞名，双--漏洞详情)
    data=[]#一个了漏洞的全部数据，包括漏洞名，漏洞详情
    lines=1# 为写入Excel做准备，从第二行写起
    xlsbook=xlsxwriter.Workbook(str(time.strftime("%Y-%m-%d_%H-%M-%S",time.localtime())+".xlsx"))
    #添加一个sheet
    sheet=xlsbook.add_worksheet()
    for dst in dst_tag.children:
        if  (not (type(dst) is bs4.NavigableString) )and repr(dst)!='\n':
            if i%2==0:
                data.append(dst.span.string)#获得漏洞名
            else:
                tbody=get_dst_tag(3,dst)
                table=get_dst_tag(1,tbody)
                host= [ a.string for a in get_dst_tag(0,table).find_all("a")]
                print "---------------host -----------------------"
                print host
                data.append(host)
                desc=get_dst_tag(2,table).td.string
                print "---------------desc -----------------------"
                print desc
                data.append(desc)
                solution=get_dst_tag(4,table).td.string
                print "---------------solution -----------------------"
                print solution
                data.append(solution)
                print "--------------------level--------------------------"
                level=float(get_dst_tag(6,table).td.string)
                if level>=7:
                    level_value="高危"
                elif level>=4:
                    level_value="中危"
                else:
                    level_value="低危"
                print level_value
                data.append(level_value)
            if(i%2==1):
                host_num=len(data[1])#获取主机的个数
                for row in range(lines,lines+host_num):#计算从第行开始写入，写几行
                    for col in range(len(data)):
                        if col !=1:
                            if  not isinstance (data[col],str ):#这地方有坑，一定要判断
                                sheet.write(row,col,unicode(data[col]))#写入主主机IP外的其他信息
                            elif isinstance (data[col], str) :
                                sheet.write(row,col,data[col].decode('utf8'))#写入主机信息
                        else :#写入主机IP
                            host_num=host_num-1 #控制主机IP的写入
                            sheet.write(row,col,unicode(data[1][host_num]))
                lines=lines+len(data[1])
                data=[]# 这个地方一定记得将数据进行清空 
            i+=1
    xlsbook.close()##数据写入完毕，进行文件的保存
#运行调用
def Run():
    html_path_list=Get_Html_PAHT_list()
    for html in html_path_list:
        html_content=ReadHtml(html)
        data_list=Get_Data(html_content)
    pass
if __name__=="__main__":
    Run()
```

### 使用说明

- 请根据脚本导入的模块，自行安装响应的模块

- 绿盟的HTML报告中将inxex.html 路径问题请参考函数def Get_Html_PAHT_list(path=os.getcwd())

- 脚本可批量处理，请指定路径

- 提供(.exe)[报告HTML转Excel(.exe下载)](http://pan.baidu.com/s/1c2tqz4W ) 密码：cnsp


推荐阅读：

- [Python调用Hashcat跑主机密码文件](http://ssjt21.github.io/2017/11/Python_Hashcatshell/)

- [Python 天融信报告HTML转Excel](http://ssjt21.github.io/2017/11/Python_Hashcatshell/)

<br>

转载请注明：[随时静听的博客](http://ssjt21.github.io) » [点击阅读原文](http://ssjt21.github.io/2017/11/Python_NSFOCUS_To_Excel/)
