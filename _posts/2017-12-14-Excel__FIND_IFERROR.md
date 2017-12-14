---
layout: post
title: "Excle FIND IFERROR函数"
date: 2017-12-14 16:32:06 
description: "Excel 中 FIND IFERROR函数得使用，根据表格中是否有某个字符串，对应得显示不同得字符串"
tag: Excel
---


根据表格中一列中是否包含某个字符串，来显示其对应得修改版本包名称

### IFERROR函数 对错误值#value！进行处理

- IFERROR(表达式,替换文本)
- 表达式表示可能出错得结果，也就是公式计算错误显示得值为#value！
- 如果是值#value！ 就会将其替换为后面得替换文本

### FIND函数  进行字符串的查找
- FIND(find\_txt,within\_txt,[start\_num])
- find_txt 查找的目标字符串不区分大小写
- within_txt 查找的范围
- start_num 从那里开始查找，默认值为1，从开头进行查找

### 例子

|包含字符串HTTP的补丁名称|包含字符串PHP的补丁名称|
|:-:|:-:|
|httpd-2.4.29或则httpd-2.2.34|php-5.6.32 或者 php-7.2.0|



```SHELL
#使用公式：
单元格B2的值： =IF(FIND("HTTP",A2),"httpd-2.4.29或则httpd-2.2.34","php-5.6.32 或者 php-7.2.0|")

```
<img src="/images/posts/Excle/FIND.gif" height="400" width="800">

```SHELL
#使用公式：
单元格B2的值： =IF(IFERROR(FIND("HTTP",A2),0),"httpd-2.4.29或则httpd-2.2.34","php-5.6.32 或者 php-7.2.0")
```
<img src="/images/posts/Excle/IFERROR.gif" height="400" width="800">


参考连接：[FIND 和 FINDDB 微软文档](https://support.office.com/zh-cn/article/FIND、FINDB-函数-c7912941-af2a-4bdf-a553-d0d89b0a0628)
--------------------------------------------------------------

推荐阅读

- [Excel VLOOKUP函数](http://ssjt21.github.io/2017/11/Excel_vlookup/)
- [Excel 根据表格内容修改格式](http://ssjt21.github.io/2017/11/Excel_ConditionFormat/)

<br>

转载请注明：[随时静听的博客](http://ssjt21.github.io) » [点击阅读原文](http://ssjt21.github.io/2017/11/Excel_FIND_IFERROR/)