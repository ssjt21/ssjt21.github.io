---
layout: post
title: "C 插入排序动图展示"
date: 2017-11-11 18:13:06 
description: "C 插入排序动图展示"
tag: C
---

### 插入排序--原理分析

- 认为前面的数字已经有序
- 将待排序的数字位置空出来,并拿出来跟前面的数字一一比较
- 当没有找到合适的位置,就一直向前找,并将比他大的数字向后移动
- 当找到比他比他小的数字后,将其数字插入到比他小的数字的后面即可
- 重复以上步骤就可进行下一个数字的的排序找到对应的合适位置
- 动图展示:
<img src="/images/posts/C/InsertSort.gif" height="400" width="850">

### 代码部分(C/C++实现)

```C++
#include <iostream>
using namespace std;
void InsertSort(int *a,int len)//插入排序
{
    int tmp;
    int j=0;
    for(int i=0;i<len;i++)
    {
       tmp=a[i+1];      //取出需要跟前面一个一个比较的数,他的位置空出来
       j=i;             //开始比较的位置,就是从tmp前面的数开始比较
       while(tmp<a[j]&&j>=0)//找到比tmp大的数就跳出循环,
       {
            a[j+1]=a[j];    //所有比tmp大的数都要向后移动
            j--;
       }               //跳出循环后,也就是a[j]大于等于tmp,所以tmp的位置就是a[j]后面也就是j+1的位置
       a[j+1]=tmp;
    }
}

int main()
{
    int a[7]={3,6,7,4,1,9,6};
    InsertSort(a,7);
    for(int i=0;i<7;i++)
    {
        cout<<a[i]<<" ";
    }
    puts("");
    return 0;
}
```


推荐阅读：

- [C 语言 练习题整理1](http://ssjt21.github.io/2017/11/C_Exercises1/)

-[C 语言 链表读写操作](http://ssjt21.github.io/2017/11/C_binary_read_write/)


<br>

转载请注明：[随时静听的博客](http://ssjt21.github.io) » [点击阅读原文](http://ssjt21.github.io/2017/11/C_InsertSort/)