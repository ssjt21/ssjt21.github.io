---
layout: post
title: "Linux Shell 三种读取文件内容的方式"
date: 2017-12-13 11:13:06 
description: "Linux Shell 三种读取文件内容的方式"
tag: Shell
---

用到对文件中数据每行的处理，这才收集了shell对文件读取的三种方法

### 使用文件重定向处理

```Shell
#!/bin/bash
filename = "./test.txt"
while read line
do
    echo $line
done < $filename
```

### 使用cat命令读取
```Shell
#!/bin/bash
filename="./test.txt"
cat $filename | while read line
do
    echo $line
done
```

### 使用命令执行 反引号
```Shell
#!/bin/bash
filename="./test.txt"
for line in `cat $filename`
do
    echo $line
done
```

### 注意

- 使用for 和 while不等价
- for 遇到空格即停止
- while 则是按一整行来读取
- 当你想处理的数据是行数据时，建议使用while





推荐阅读：

- [Linux 系统目录结构](http://ssjt21.github.io/2017/11/Linux_DirStruct/)

- [Linux 获取系统登陆用户密码的加密方式](http://ssjt21.github.io/2017/11/Linux_DirStruct/)


<br>

转载请注明：[随时静听的博客](http://ssjt21.github.io) » [点击阅读原文](http://ssjt21.github.io/2017/12/Shell_Readfile/)

