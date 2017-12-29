---
layout: post
title: "C 语言 链表读写操作"
date: 2017-12-29 18:51:06 
description: "C 结构体-链表二进制得方式写入文件和读取"
tag: C
---

### 链表写入文件和读取
- 写入数据得大小是否包括next指针，读写要一致；
- 读数据得过程就是将文件中的数据一个一个读取，实质是创建链表的过程，只不过数据的来源是文件，但是指针中的值是垃圾值，需要单独处理构建链表；


### struct 链表以二进制得方式写入文件和读取
```C++
#include<iostream>
using namespace std;
#include<string.h>
#include<stdlib.h>
#include<fstream>

struct node
{
    int score[3];
    char name[20];
    struct node *next;
};

void save(struct node *head)//传入链表得首地址
{
    struct node* p=head;
    fstream iostrf;//定义文件流对象用于对文件得读写
    iostrf.open("stuf.dat",ios::out|ios::binary);
    if(!iostrf.is_open())//判断打开文件是否成功
    {
        exit(0);//不成功就退出程序
    }
    while(p)//链表不为空就执行循环写入文件
    {//这里得写入数据大小可以改一下将指针部分得数据去掉：write((char*)p,sizeof(*p)-sizeof(p->next));
    //但是，记得读文件时得操作，也是读这么个大小，不要读多了
        iostrf.write((char*)p,sizeof(*p));
        cout<<"........"<<endl;
        p=p->next;//移动到下一个节点
    }
    iostrf.close();//记得文件打开后一定要关闭
}
//将数据从文件中数据读入链表，实际上是创建得链表得过程
//只不过是数据得获取不再是输入端而是从文件
struct node* load_data()
{
    struct node* head=NULL,*p=NULL,*pr=NULL;
    fstream  iostrf;
    iostrf.open("stuf.dat",ios::in|ios::binary);
    if(!iostrf.is_open())
    {
        exit(0);
    }
    head=p=pr=new node;//申请内容用于存放数据
    for(;iostrf.read((char*)p,sizeof(*p));)//从文件读取数据放入*p中
    {
        pr->next=p;
        p->next=NULL;
        pr=p;
        p=new node;
    }
    iostrf.close();
return head;
}
void display(struct node* head)//暑促链表中得数据
{
    struct node *p=head;
    while(p)
    {
        cout<<p->score[0]<<" ";
        cout<<p->score[1]<<" ";
        cout<<p->score[2]<<" ";
        cout<<p->name<<endl;
        p=p->next;
    }
}
int main()
{
    struct node* head,*p;

    // p=head=new node;
    // p->score[0]=11;
    // p->score[1]=22;
    // p->score[2]=33;
    // strcpy(p->name,"xioaming");

    // p=new node;
    // p->score[0]=55;
    // p->score[1]=66;
    // p->score[2]=77;
    // strcpy(p->name,"hello");
    // head->next=p;
    // p->next=NULL;

    // p=new node;
    // p->score[0]=88;
    // p->score[1]=66;
    // p->score[2]=99;
    // strcpy(p->name,"hello");
    // head->next->next=p;
    // p->next=NULL;
    head =load_data();
    display(head);
    // save(head);
    return 0;
}
```
推荐阅读：

- [C 语言 练习题整理1](http://ssjt21.github.io/2017/11/C_Exercises1/)

- [C 语言 插入排序 ] (http://ssjt21.github.io/2017/11/C_InserSort/)


<br>

转载请注明：[随时静听的博客](http://ssjt21.github.io) » [点击阅读原文](http://ssjt21.github.io/2017/11/C_binary_read_write/)

