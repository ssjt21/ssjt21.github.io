---
layout: post
title: "Linux 获取系统登陆用户密码的加密方式"
date: 2017-11-16 11:46:06 
description: "Linux 破解密码如何查询系统用户密码的加密方式"
tag: Linux
---

每次跑弱口令都会很纠结，主机的加密方式，虽然根据密文的一些特征能够做出简单的判断，可是还是有一些密码的密文的加密方式无法确定，找遍网上教程也没找到合适的方法，特地找了一下Linux中的加密函数，结果获取了意外的惊喜！

### man手册帮助命令查看 crpyt函数说明

`root@localhost:~# man crypt`

<img src="/images/posts/Linux/Linux_get_sys_crypt.gif" height="450" width="800">

从上面额图片中我们看出passwd程序使用的加密方法就是crypt()函数，所以根据crypt下面的介绍，结合 /etc/shadow文件中密文的格式就可以确定了

```C++
//Linux 下 对传入的参数加密使用固定的salt:$6$4KaYW63o$
// get_crypt.c
#define _XOPEN_SOURCE
#include<stdio.h>
#include<unistd.h>
#include<stdlib.h>
#include<string.h>
int  main(int argc,char*argv[])
{
	char * passwd;
	char *key=argv[0];
	if(strlen(key)!=0)
	{
		passwd=crypt(key,"$6$4KaYW63o$");
		printf("the salt:$6$4KaYW63o$\n");
	  	printf("password:%s\n",passwd);
	}
	else
	{
		printf("Please input your encrypt string\n");
		printf("The using: ./get_crypt 'the string you need encrypt'\n");
	}
	
	return 0;
}
//编译方式： gcc  get_crypt.c -lcrypt -o get_crypt
//运行方式：./get_crypt "123456"
```







推荐阅读：

- [Linux 获取系统登陆用户密码的加密方式](http://ssjt21.github.io/2017/11/Linux_Get_SYS_CryptMode/)


<br>

转载请注明：[随时静听的博客](http://ssjt21.github.io) » [点击阅读原文](http://ssjt21.github.io/2017/11/Linux_DirStruct/)










