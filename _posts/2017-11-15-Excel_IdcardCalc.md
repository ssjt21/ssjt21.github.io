---
layout: post
title: "Excel 通过身份证号计算性别出生日期年龄"
date: 2017-11-15 10:13:06 
description: "Excel 中 通过身份证号计算性别出生日期年龄,IF函数,MID函数,MOD函数,TEXT函数,TODAY函数,DATEDIF函数"
tag: Excel
---

跟大家分享一下Excel中IF,MID,MOD,TEXT,DATEDIF,TODAY函数的使用方法以及利用这些函数来根据省份证号计算性别,出生日期,年龄.

### MID(text,start\_num,char\_nums) 截取字符串
- text,指定区域或者字符串
- start_num,截取字符串开始的位置
- char_nums,截取字符串的个数

### MOD(m,n) m对n求余数
- 数m对n求余数,余数的符号和n相同
- eg: MOD(3,-2)的结果是 -1

### TEXT(value,format\_txt)将数值转换成指定的格式 


|Value|Format\_text|结果|说明|
|-|:-|:-|:-|
|10.15|"000.0"|010.2|小数点前不够三位用0补齐，保留一位小数，不足一位用0补齐|
|10.00|####|10|没用的0一律丢弃|
|1.253|00.##|01.25|小数点前不足两位用0补齐，保留两位，不足两位不补位|
|1|正数;负数;零|正数|大于0为正数,小于0为负数,等于0为零|
|19820506|0000-00-00|1982-05-06|按所示形式显示日期|
|19820506|0000年00月00日|1982年05月06日|按所示形式显示日期|
|2014/3/1|aaaa|星期六|显示为中文星期几全称|
|2014/3/1|aaa|六|显示为中文星期几简称|
|2014/3/1|dddd|Monday|显示为英文星期几全称|
|80|[>=90]优秀;[>=60]及格;不及格|及格|根据值输出对应的等级|
|123|[DBNum1][$-804]G/通用格式|一百二十三|中文小写数字|
|123|[DBNum2][$-804]G/通用格式元整|壹佰贰拾叁元整|中文大写数字，并加入“元整”字尾|
|123|[DBNum3][$-804]G/通用格式|1百2十3|中文小写数字|
|19|[>20][DBNum1];[DBNum1]d|十九|11-显示为十一而不是一十一|

### DATEDIF(start\_date,end\_date,unit) 返回两个日期之间的间隔数

- start\_date,表示起始日期
- end\_date,表示结束的日期
- unit, 返回时间单位的代码

--------------------------------------------------

|unit值|说明|
|:-:|:-|
|Y|返回时间值按整年计算|
|M|返回时间值按整月计算|
|D|返回时间值按整天计算|
|MD|起始日期与结束日期的同月间隔天数。 忽略日期中的月份和年份|
|YD|起始日期与结束日期的同年间隔天数。忽略日期中的年份。|
|YM|起始日期与结束日期的间隔月数。忽略日期中年份|


#### DATEDIF 例子

|功能描述|公式|结果|
|:-|:-|:-:|
|计算出生日期为1980-4-1人的年龄|=DATEDIF("1980-4-1",TODAY(),"Y")|37|
|计算日期为1980-4-1和当前日期的间隔的月数|=DATEDIF("1980-4-1",TODAY(),"M")|451|
|计算日期为1980-4-1和当前日期的间隔的天数|=DATEDIF("1980-4-1",TODAY(),"D")|13742|
|计算日期为1980-4-1和当前日期的间隔的天数不计年数差|=DATEDIF("1980-4-1",TODAY(),"YD")|228|
|计算日期为1980-4-1和当前日期的间隔的天数不计月数差|=DATEDIF("1980-4-1",TODAY(),"MD")|14|
|计算日期为1980-4-1和当前日期的间隔的月数不计年数差|=DATEDIF("1980-4-1",TODAY(),"YM")|7|


### TODAY() 返回当前的额日期

|功能描述|公式|
|:-|:-|
|返回当前日期加5天|=TODAY()+5|
|返回当前年|=YEAR(TPDAY())|
|返回当前月(1-12)|=MONTH(TODAY())|
|返回当天(1-31)|=DAY(TPDAY())|

### 身份证号含义解释

|位数|解释|
|:-|:-|
|1-2|所在省份的代码|
|3-4|所在城市的代码|
|5-6|所在区县的代码|
|7-14|出生年月日|
|15-16|所在地派出所代码|
|17|性别标识,奇数(男),偶数(女)|
|18|校验码,通过前面的17位计算的来的,用来检验身份证的正确性。校检码可以是0~9的数字，有时也用x表示.|

### Excel 通过公式计算性别、出生日期、年龄

|公式|说明|
|:-|:-|
|=IF(MOD(MID(A2,17,1),2),"男","女")|计算性别|
|=TEXT(MID(A2,7,8),"000-00-00")|计算出生日期|
|=DATEDIF(TEXT(MID(A2,7,8),"0000-00-00"),TODAY(),"Y")|计算年龄|
|=DATEDIF(C2,TODAY(),"Y")|计算年龄|


<img src="/images/posts/Excle/Excel_DATEDIF_IF_TEXT.gif" height="400" width="800">


-------------------------------------------------

推荐阅读：

- [Excel VLOOKUP函数](http://ssjt21.github.io/2017/11/Excel_vlookup/)
- [Excel 根据表格内容修改格式](http://ssjt21.github.io/2017/11/Excel_ConditionFormat/)


<br>

转载请注明：[随时静听的博客](http://ssjt21.github.io) » [点击阅读原文](http://ssjt21.github.io/2017/11/Excel_IdcardCalc/)