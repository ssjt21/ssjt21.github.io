---
layout: post
title: "C 语言 练习题整理1"
date: 2017-11-5 20:30:06 
description: "C 整理一些特别的C语言习题帮助加深对C语言的快速理解！"
tag: C
---

为了快速理解C语言的语法特别整理的一些典型例子。在学习过程中遇到任何C语言问题都可以联系博主寻求帮助！Email:d1314ziting@163.com

### switch case 语句

``` C
//----- 1 --------
#include<stdio.h>
int main()
{
    int i=0,a;
    for(a=0;a<2;a++)
    {
        switch(a)
        {
            case 1:i+=1;       
            case 2:i+=2;
            default:i+=3;
        }
    }
    printf("%d",i);
    return 0;
}
//运行结果：9

//----- 2 --------
#include<stdio.h>
int main()
{
    int a=0,i=0;
    for(i=1;i<5;i++)
    switch(i)
    {
        case 0:;
        case 3: a+=2;
        case 1: ;
        case 2: a+=3;
        default: a+=5;    
    }
    cout<<a<<endl;
    return 0;
}
//运行结果：31

//----- 3 --------
```

### 指针数组 

``` C
//----- 1 -------
#include<stdio.h>
#include <string.h>
int main()
{
    char *c[]={"1234cc","12ddddd3","456","456","123"};
    printf("%d,%d,%s",strlen(*c),sizeof(c),*c+1);
    return 0;
}
//运行结果：6,20,234cc
```

### define 预定义

``` C
//----- 1 -------
#include<iostream>
#define A(X) X;X;X;X;X;
using namespace std;
int main()
{
    int i=0;
    A(A(A(i++)));
    cout<<i;
    return 0;
}
//运行结果：125
```

### scanf()、 putchar()、getchar()函数

```C
//----- 1 -----
#include<stdio.h>
int main()
{   //输入123<回车>45678<回车>
    char c1,c2,c3,c4,c5,c6;
    scanf("%c%c%c%c",&c1,&c2,&c3,&c4);
    c5=getchar();c6=getchar();
    putchar(c1);putchar(c2);
    printf("%c%c\n",c5,c6);
    return 0;
}
//结果：1245
```

### ++ -- while for

``` C
//----- 1 -------
#include<stdio.h>
int main()
{   
    int a=1,b=10;
    do
    {
        b-=a;
        a++;
    }while(b--<0);
    printf("%d",b);
    return 0;
}
//结果 ： 8

//----- 2 -------
#include<stdio.h>
int main()
{   
    int x=3;
    do
    {
        printf("%d",x-=2);
    }while(!(--x));
    return 0;
}
//运行结果： 1-2

//----- 3 -------
#include<stdio.h>
int main()
{   
    int i,j,x=0;
    for(i=0;i<2;i++)
    {
        x++;
        for(j=0;j<=3;j++)
        {
            if(j%2)
                continue;
            x++;
        }
        x++;
    }
    printf("x = %d\n",x);
    return 0;
}
//运行结果：x = 8

//------ 4 --------
#include<stdio.h>
int main()
{   
    int i,s=0;
    for(i=2;;i++)
        if(!(i%4))break;
    else s+=i;
    printf("%d",s);
    return 0;
}
//运行结果：5

//------ 5 --------
#include<stdio.h>
int main()
{   
    int i=0,a=0;
    while(i<20)
    {
        for(;;)
            if(i%10==0)
            break;
        else i--;
        i+=11; a+=i;
    }
    printf("%d\n",a);
    return 0;
}
//运行结果：32
```

### 逻辑短路 || &&

```C
#include<stdio.h>
int main()
{   
    int i=0,j=0,a=6;
    if((++i>0) || (++j>0))
        a++;
    printf("i = %d,j = %d,a = %d\n",i,j,a);
    return 0;
}
//运行结果：i = 1,j = 0,a = 7
```

### 运算符优先级

```C
//------ 1 -------
#include<stdio.h>
int main()
{   
    int a=4,b=5,c=0,d;
    d=!a&&!b||!c;
    printf("%d\n",d);
    return 0;
}
//运行结果：1
```
推荐链接：

- [Editplus的安装激活和汉化](http://d1314ziting.blog.163.com/blog/static/25551704320164184458513/)
- [Editplus Mingw配置c c++](http://d1314ziting.blog.163.com/blog/static/255517043201641763711409/)
- [Easy Graphics Engine & vs2015 安装使用](http://d1314ziting.blog.163.com/blog/static/255517043201671410242847/)



<br>

转载请注明：[随时静听的博客](http://ssjt21.github.io) » [点击阅读原文](http://ssjt21.github.io/2017/11/C_Exercises1/)