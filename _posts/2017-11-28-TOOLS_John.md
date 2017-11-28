--- 
layout: post
title: "KALI John破解工具的使用"
date: 2017-11-28 14:34:06 
description: "KALI John破解工具的使用"
tag: Tools
---

### 介绍

&nbsp;&nbsp;&nbsp; John the Ripper免费的开源软件，是一个快速的密码破解工具，用于在已知密文的情况下尝试破解出明文的破解密码软件，支持目前大多数的加密算法，如DES、MD4、MD5等。它支持多种不同类型的系统架构，包括Unix、Linux、Windows、DOS模式、BeOS和OpenVMS，主要目的是破解不够牢固的Unix/Linux系统密码。目前的最新版本是John the Ripper 1.8.0版，针对Windows平台的最新免费版为John the Ripper 1.7.9版。

### 下载

`Windows地址:`
	
链接：[http://pan.baidu.com/s/1c2rowU0] (http://pan.baidu.com/s/1c2rowU0) 密码：npoj

Kali中无需下载直接使用
其他Linux请使用命令：
`sudo apt-get install john
或
	sudo yum install –y john`
请记得连上互联网！

### John破解模式

- 字典模式：在这种模式下，用户只需要提供字典和密码列表用于破解。
- 单一破解模式：这是john作者推荐的首选模式。John会使用登录名、全名和家庭通讯录作为候选密码。
- 递增模式：在该模式下john会尝试所有可能的密码组合。这是最具威力的一种。
- 外部模式：在这种模式下，用户可以使用john的外部破解模式。使用之前，需要创建一个名为（list.external:mode）的配置文件，其中mode由用户分配。

`破解条件：已知密文`

**破解过程中推荐的破解模式顺序**

单一模式(single) --> 字典模式(wordlist) --> 递增模式(incremental)  --> 默认模式

### 字典模式 - -worldlist

```C
#命令方式：john --wordlist=wordlst.txt  pass_shadow.txt
#wordlst.txt:是字典文件，每个密码独占一行
#pass_shadow.txt:密码文件，需要root用户下使用命令unshadow /etc/passwd /etc/shadow > pass_shadow.txt 来合并passwd文件和shadow文件到一个文件中
#

#查看结果：john  --show pass_shadow.txt


#仅破解指定的用户： 
#john --wordlist=wordlst.txt  --users=root,ftp,httpd pass_shadow.txt 

#仅破解有登陆权限的用户：
#john --wordlist=wordlst.txt --shells=/usr/sbin/nologin pass_shadow.txt
#显示破解出指定用户的密码：
#john --users=root,webadmin pass_shadow.txt --show
```

### 单一模式 - -single
```C
#命令方式： john --single  pass_shadow.txt
#pass_shadow.txt:从这里就不多说了，上面解释过了
#破解指定的用户的密码：
#john --single  --users=root,webadmin  pass_shadow.txt
#
#破解指定的加密方式的密码：
#john --single  --format=aix-ssha512  pass_shadow.txt
#
#// 查看 --format 可以指定的加密类型
#john --list=formats

```

### 递增模式

```javascript
#注意：一般不适用，太过强大需要很长得时间，你等不起
#全部密码破解模式：
#john --incremental pass_shadow.txt
#
#使用数字：
#john –incremental:digits pass_shadow.txt
#
#数字6位：
#john –incremental:digits 6 pass_shadow.txt
```

### 扩展模式

```C
#过滤掉字典中出现得数字：
#john --external=Filter_digits --wordlist=wordlst.lst pass_shadow.txt
# 
#更多详细得信息请见：more /etc/john/john.conf
#查看external列表
#john --list=external
```

### 其他使用方式

```C
#比如我们想破解 SQL Server2005 数据库得密码
#第一种方式：
#自动识别加密方式
#john --wordlist=wordlst.lst ssql.pass
#第二种：
#list帮助：
#john --list=help
#
#查看所有得加密方式：
#john --list=formats

#查询SQL Server 对应得版本加密参数
```
### `--help`

```C
John the Ripper password cracker, version 1.8.0.6-jumbo-1-bleeding [linux-x86-64-avx]
Copyright (c) 1996-2015 by Solar Designer and others
Homepage: http://www.openwall.com/john/

#1.	Usage: john [OPTIONS] [PASSWORD-FILES]
#2.	--single[=SECTION]        "single crack" mode
#3.	--wordlist[=FILE] --stdin wordlist mode, read words from FILE or stdin
#4.	--pipe  like --stdin, but bulk reads, and allows rules
#5.	--loopback[=FILE]         like --wordlist, but fetch words from a .pot file
#6.	--dupe-suppression        suppress all dupes in wordlist (and force preload)
#7.	--prince[=FILE]           PRINCE mode, read words from FILE
#8.	--encoding=NAME           input encoding (eg. UTF-8, ISO-8859-1). See alsodoc/ENCODING and --list=hidden-options.
#9.	--rules[=SECTION]         enable word mangling rules for wordlist modes
#10.	--incremental[=MODE]      "incremental" mode [using section MODE]
#11.	--mask=MASK               mask mode using MASK
#12.	--markov[=OPTIONS]        "Markov" mode (see doc/MARKOV)
#13.	--external=MODE           external mode or word filter
#14.	--stdout[=LENGTH]         just output candidate passwords [cut at LENGTH]
#15.	--restore[=NAME]          restore an interrupted session [called NAME]
#16.	--session=NAME            give a new session the NAME
#17.	--status[=NAME]           print status of a session [called NAME]
#18.	--make-charset=FILE       make a charset file. It will be overwritten
#19.	--show[=LEFT]             show cracked passwords [if =LEFT, then uncracked]
#20.	--test[=TIME]             run tests and benchmarks for TIME seconds each
#21.	--users=[-]LOGIN|UID[,..] [do not] load this (these) user(s) only
#22.	--groups=[-]GID[,..]      load users [not] of this (these) group(s) only
#23.	--shells=[-]SHELL[,..]    load users with[out] this (these) shell(s) only
#24.	--salts=[-]COUNT[:MAX]    load salts with[out] COUNT [to MAX] hashes
#25.	--save-memory=LEVEL       enable memory saving, at LEVEL 1..3
#26.	--node=MIN[-MAX]/TOTAL    this node's number range out of TOTAL count
#27.	--fork=N                  fork N processes
#28.	--pot=NAME                pot file to use
#29.	--list=WHAT               list capabilities, see --list=help or doc/OPTIONS
#30.	--format=NAME             force hash of type NAME. The supported formats        can be #31     seen with --list=formats and --list=subformats
```


推荐阅读：

- [KALI Hydra破解工具的使用](https://ssjt21.github.io/2017/11/TOOLS_Hydra/)

- [Tkinter Canvas控件使用-3](https://ssjt21.github.io/2017/11/Python_TK_Canvas/)

- [Python PIL Image类使用](http://ssjt21.github.io/2017/11/Python_PIL_Image_Module/)

- [Python调用Hashcat跑主机密码文件](http://ssjt21.github.io/2017/11/Python_Hashcatshell/)



<br>

转载请注明：[随时静听的博客](http://ssjt21.github.io) » [点击阅读原文](https://ssjt21.github.io/2017/11/TOOLS_John/)