---
layout: post
title: "Python调用Hashcat跑主机密码文件"
date: 2017-11-3 15:13:06 
description: "工作中为了解决繁琐的重复性工作提高工作效率，写了个调用hashcat批量跑主机密码的脚本"
tag: Python
---

Python 调用Hashcat64.exe 来批量跑主机密码文件。

### Python实现代码

```Python
# -*- coding:utf-8 -*-
import re #匹配 IP 文件名中的IP ，匹配hash值和用户名
import glob #文件路径处理
import os   #文件操作
import time #文件命名规则适用
import sys #参数获取

#获取当前的工作目录（脚本）
current_dir=os.getcwd()
print "## Current workdir is :",current_dir

#获取放置shadow文件的文件夹
def Getshadowdir():
    if len(sys.argv)==4:
        shadowdir=sys.argv[1]
        shadowdirpath=os.path.join(current_dir,shadowdir)
        print "Paragram shadowdir:shadowdir is ",shadowdirpath
        return shadowdirpath
    else:
        print "Please input the shawdowdir name for the first paragram!"
        print "PS:The shell and shadowdir in same dir!"
        print "The shell exit for paragram less error!"
        sys.exit()

#获取hashcat64.exe的路径
def Gethashcat_bin():
    if len(sys.argv)==4:
        hashcatdir=sys.argv[2]
        hashcatdir=os.path.join(current_dir,hashcatdir)
        print "Paragram hashcat64.exe :hashcat64.exe dir is ",hashcatdir
        return hashcatdir
    else:
        print "Please input the hashcat64.exe dirname for second paragram! "
        print "PS:The shell and  hashcat64.exe dirname in same dir!"
        print "The shell exit for paragram less error!"
        sys.exit()
    
#获取字典文件的路径
def Getpasswd():
    if len(sys.argv)==4:
        password=sys.argv[3]
        password=os.path.join(current_dir,password)
        print "Paragram password:password is ",password
        return password
    else:
        print "Please input the password for third paragram! "
        print "PS:The shell and  password in same dir!"
        print "The shell exit for paragram less error!"
        sys.exit()

#获取所有shadow文件完整路径
def Getshadows(path,shadowlst):
    for fn in glob.glob(path+os.sep+"*"):
        shadowlst.append(fn)


#根据文件名获取shadow文件对用的IP
def Getip(path):
    pattern=re.compile('.*?(?P<ip>(\d+\.){3}\d+).*?')
    filename=os.path.basename(path)
    match=pattern.match(filename)
    return match.group('ip')
#获取用户名和hash值
def getuser_hash(path):
    pass
#-------------------------
#hashcat64.exe -a 0 -m 1800 shadowfile wordlst
#hashcat64.exe -a 0 -m 1800 shadowfile wordlst --show
# #-------------------------
def run1():
    shadowlst=[]
    shadowdirpath=Getshadowdir()#获取shadow文件夹
    hashcat64_bin=os.path.join(Gethashcat_bin(),'hashcat64.exe')#获取hashcat64.exe路径
    password=Getpasswd()#获取字典文件路径

    Getshadows(shadowdirpath,shadowlst)#获取shadow文件的路径

   
    getresult=''
    for shadow in shadowlst:
        print '-- shadow file path:',shadow
        hash_bin=hashcat64_bin+" -a 0 -m 1800 "+shadow+" "+password
        print hash_bin
        os.system(hash_bin)
        # print '** the ip for shadow:',Getip(shadow)
        
    pass
def run2():
    shadowlst=[]
    shadowdirpath=Getshadowdir()#获取shadow文件夹
    hashcat64_bin=os.path.join(Gethashcat_bin(),'hashcat64.exe')#获取hashcat64.exe路径
    password=Getpasswd()#获取字典文件路径

    Getshadows(shadowdirpath,shadowlst)#获取shadow文件的路径

   
    # f=open('result.txt',w)
    for shadow in shadowlst:
        print '-- shadow file path:',shadow
        ip=Getip(shadow)
        os.system('echo '+ip +" >> result.txt")
        hash_bin=hashcat64_bin+" -a 0 -m 1800 "+shadow+" "+' --show >> result.txt'
        print hash_bin

        os.system(hash_bin)
        # print '** the ip for shadow:',Getip(shadow)
    # f.close()
    pass
def run():
    print "-------------------------------------------------------------"
    print "Use for run hashcat: shell.exe shadowdir  hashcatdir dic.lst "
    print "--------------------------------------------------------------"
    print "##  Please select option:"
    print "**  1. run hashcat64.exe"
    print "**  2. run get result"
    print "##  Enter others key to exit!"
    print '''Version 1.0 
            Any question! QQ:1260945877  or Email:d1314ziting@16.com'''
    
    option=int(input("select:"))
    if option==1:
        run1()
        return True
    elif option==2:
        run2()
        return True
    else:
        return False
def main():
    while not run():
        pass
main()
```
### 使用方法
1. 使用前请确认hashcat破解模式和破解密码的类型
2. 请将脚本文件放到hashcat.exe的上级目录
3. 请将密码文件目录和脚本放置同级目录
4. 请将字典和脚本放置同级目录
5. 请确保已经装了Python
6. CMD命令下进入脚本目录
7. 执行命令： Pyhton 脚本文件 存放shadow文件的目录 包含hashcat.exe的目录 字典文件


> 注：shadown文件名中必须包含主机IP或者自己修改代码正则表达式，修改符合自己需要的匹配模式

推荐阅读：

- [Python 天融信报告HTML转Excel](https://ssjt21.github.io/2017/11/Python_HtmltoExcel/)

- [Python 绿盟HTML报告转Excel](https://ssjt21.github.io/2017/11/Pyton_NSFOCUS_To_Excel/)

<br>

转载请注明：[随时静听的博客](http://ssjt21.github.io) » [点击阅读原文](http://ssjt21.github.io/2017/11/Python_Hashcatshell/)