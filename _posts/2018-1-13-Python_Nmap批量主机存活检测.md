--- 
layout: post
title: "Python Nmap批量主机存活检测脚本"
date: 2018-1-13 9:25:06 
description: "Python 调用Nmap批量检测主机存活并导出Excel统计表"
tag: Python
---

吉林移动网络管理中心项目实施2018-1-13

### 脚本主要功能

- 批量检测IP.txt文件中的ip是否存活，IP.txt中数据的格式是每行一个IP或网段
- 检查结果导出XML和ExceL，并将汇总结果导出至host_up.xls中
- host\_up\_test.py,调用nmap进行主机存活检测，并导出XML格式的文件，需要在get\_result.py之前运行
- get\_result.py 从xml中读取数据写入Excel并汇总存活主机数量

### 脚本运行环江

- pyexcel_xls，请移步[Python pyexcel-xls使用](https://ssjt21.github.io/2018/1/Python_Pyexcel-xls/)

- Windows操作系统

- nmap已安装并配置了环境变量

### host\_up\_test.py 脚本内容
```python
# -*- coding: utf-8 -*-

import os
import re
import time
def get_ip(filename="./IP.txt"):
    # 去重复的
    IP=set()
    I=0
    with open(filename) as ips:
        for ip in ips:
            I=I+1
            IP.add(ip.strip())
    if I==len(IP):
        print "数据总数是：",I,len(IP),"没有重复数据"
    else:
        print "存在重复的数据：",I-len(IP)
    return IP

IP_set=get_ip()

def use_nmap(ip,command="-sP -sn -PE -PP -PM -PS -PA -PU -PY"):
    com="nmap "+command+" "+ip+" -oX "+ip.replace('/','-')+".XML"
    print com
    os.system(com)

def run():
    
    for ip in get_ip():
        
        use_nmap(ip,'-sn -sP')
    
    print "complete..."
    
run()
```
### get\_result.py
```python
# -*- coding: utf-8 -*-
import re
import os
import xml.dom.minidom
import glob
from collections import OrderedDict
from pyexcel_xls import get_data,save_data

try:
    import xml.etree.cElementTree as ET 
except ImportError:
    import xml.etree.ElementTree as ET 

def get_xml_file():
    return glob.glob('*.XML')
print "当前XML文件数量：",len(get_xml_file())

def parse_xml(filename="111.26.23.0-25.XML"):
    try:
        tree=ET.parse(filename)
        root=tree.getroot()
    except Exception,e:
        print "Error:can not  parse file:",filename
        sys.exit(1)
    # print root.tag,root.attrib
    scan_dic=root.attrib
    command=scan_dic['args']#扫描使用的命令
    nmap_version=scan_dic['scanner']+":"+scan_dic['version']#扫描时用的nmap版本
    start_time=scan_dic['startstr']#扫描的时间
    hosts=OrderedDict()
    for child in root:
        # print child.tag,child.attrib
        if child.tag=="host":
            up_down=child[0].attrib['state']#主机存活标志
            ip=child[1].attrib['addr']#获取主机IP地址
            hosts[ip]=up_down#添加入有序字典中
        elif child.tag=="runstats":
            # print child
            up_ip_num=child[1].attrib['up']#存货啊主机的个数
            down_ip_num=child[1].attrib['down']
            total_ip_num=child[1].attrib['total']
        basename=os.path.basename(filename)
        xls_name=os.path.splitext(basename)[0]+".xls"
    return (xls_name,command,nmap_version,start_time,hosts,up_ip_num,down_ip_num,total_ip_num)

def write_Excel(data):
    table=OrderedDict()
    sheet=[]
    xls_name=data[0]
    sheet_name=os.path.splitext(xls_name)[0]
    sheet.append([u"扫描目标",sheet_name.replace('-','/'),u"命令:",data[1],u"Nmap版本",data[2],u"启动时间",data[3]])
    # print data[4]
    if data[4]:
        for ip,item in data[4].items():
            print ip,item
            sheet.append([ip,item])
    sheet.append([u"存活主机个数:",data[5],u"down 主机个数:",data[6],u"检测主机总数:",data[7]])  
    # print sheet
    table.update({sheet_name:sheet})
    save_data(xls_name,table)

def write_Excel_all(data_list):
    table=OrderedDict()
    sheet=[]
    xls_name=u"up_host.xls"
    sheet_name=u"存活主机统计表"
    up_num=0
    down_num=0
    total_num=0
    for data in data_list:
        # print data
        if data[4]:
            for ip,item in data[4].items():
                print ip,item
                sheet.append([ip,item])
        up_num=up_num+int(data[5])#存活主机个数统计
        down_num=down_num+int(data[6])
        total_num=total_num+int(data[7])#扫描主机个数统计
    sheet.append([u"存活主机个数:",up_num,u"down 主机个数:",down_num,u"扫描主机总数:",total_num])
    table.update({sheet_name:sheet})
    save_data(xls_name,table)    #写入文件
        
def run():
    xml_file_list=get_xml_file()#获取当前目录下的所有XML文件
    # print xml_file_list
    data_list=[]
    for xml in xml_file_list:
        data=parse_xml(xml)
        data_list.append(data)
       
        write_Excel(data)
    write_Excel_all(data_list)
    print "completed...."

run()
```


推荐阅读：

- [Tkinter Button控件使用-2](https://ssjt21.github.io/2017/11/Python_TK_Button/)


- [Python PIL Image类使用](http://ssjt21.github.io/2017/11/Python_PIL_Image_Module/)

- [Python调用Hashcat跑主机密码文件](http://ssjt21.github.io/2017/11/Python_Hashcatshell/)



<br>

转载请注明：[随时静听的博客](http://ssjt21.github.io) » [点击阅读原文](https://ssjt21.github.io/2018/1/Python_Nmap批量主机存活检测/)
