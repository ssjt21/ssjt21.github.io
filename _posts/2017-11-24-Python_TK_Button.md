--- 
layout: post
title: "Tkinter Button控件使用-2"
date: 2017-11-24 13:13:06 
description: "Python Tkinter Button按钮的使用例子"
tag: Tkinter
---


### Tkinter Button控件使用举例
```Python
# -*- coding: utf-8 -*-
from tkinter import *

#Button控件
# 1. 可以存放图片或者文本再或者是图片文本
# 2. 文本字体是统一字体类型
# 3. 文本可跨越多行使用\n
# 4. 可以使用tab键进行按钮的切换
# 5. 文本可以加下划线
# 6. 可以绑定事件-工具栏和

# 例子1--绑定事件
root=Tk()
root.geometry("600x400")

def callback():
    print "Clicked!"

btn=Button(root,text="点击",command=callback,fg="red")
#绑定事件，也可以将command参数在创建按钮中指定
btn.configure(command=callback)
#居左显示 side可选值：LEFT RIGHT TOP CENTER BUTTOM
btn.pack(side=LEFT)

# 例子2 state padx pady
#padx,pady分别设置文本和空间边框的距离，默认是根据内容自动显示
# state指定按钮的状体为禁用 可选值有：NORMAL,ACTIVE,
btn2=Button(root,text="禁用",padx=10,pady=20,state=DISABLED)
btn2.pack(side=RIGHT)


#例子3
frame=Frame(root,width=100,height=90)
#使用pack_propagate可以让frame不根据空间的大小改变，固定frame的宽和高
frame.pack_propagate(0)
frame.pack()

btn3=Button(frame,text="Frame上的按钮")
#将布满整个容器中
btn3.pack(fill=BOTH,expand=1)


#例子4
# 多行文本4.1
# anchor,指定文本在空间上的位置：N,NE,E,SE,S,SW,W,NW,CENTER(默认值)
#justify对其方式
#使用\n显示多行文本
btn4=Button(root,text="多行文本-多行文本-多行文本\n-多行文本-多行文本-多行文本-多行文本-多行文本\n-多行文本-多行文本-多行文本-多行文本-多行文本-",justify=RIGHT,anchor=W,padx=10)
btn4.pack(side=LEFT)
#使用wraplength 设置多行显示，根基屏幕单位显示
btn41=Button(root,text="多行文本2多行文本2多行文本2多行文本2多行文本2多行文本2多行文本2多行文本2",wraplength=100,font=("Courier New",10))
btn41.pack()

# 例子5
# relief的值SUNKEN,RAISED,GROOVE,FLAT
# 设置按钮的样式
btn5=Button(root,text="像被按下的按钮",relief=SUNKEN)
btn5.pack(side=LEFT)


#例子6
#创建一个文件对象
#compound指定text和image的关系
# CENTER:text会在image上面
# LEFT:image在text左边，RIGHT,TOP,BUTTOM依次类推
image=PhotoImage(file="demo.gif")
btn6=Button(root,text="图片",image=image,compound=TOP)
btn6.pack(side=BOTTOM)



# 例子7
# activebackground ：设置控件被激活时的背景颜色
# activeforeground : 设置控件被激活时的前景颜色（字体
btn7=Button(root,text="例子7",activebackground="green",activeforeground="yellow")
btn7.pack()

# 例子8
# bd或者bordwidth ：控件边框的大小
# bg或background  : 设置控件的背景颜色
# fg或则foreground : 设置控件的前景颜色(字体的颜色设置)
# underline :默认值为-1,设置text是否加入下划线,下标从0开开始.只对一个字符加下划线
btn8=Button(root,text="例子8",padx=10,pady=20)
btn8.configure(bd=4)
btn8.configure(bg="white")
btn8.configure(fg="purple")
btn8.configure(underline=1)#对字符"子"加下划线
btn8.pack()

# 例子9
# StringVar：变量绑定
# var.set() ：设置btn9 text的值
# var.get() : 获得btn9 text的值
# width,height :控件的大小可变，width，height是最大值
var=StringVar()
btn9=Button(root,textvariable=var,width=30,height=50)
var.set("例子9")
print var.get()
btn9.pack()

root.mainloop()
```
<img src="images/Python/Tkinter/Button/Tkinter_Button_1.jpg" width="600" height="500">




推荐阅读：

- [Python PIL Image类使用](http://ssjt21.github.io/2017/11/Python_PIL_Image_Module/)

- [Python调用Hashcat跑主机密码文件](http://ssjt21.github.io/2017/11/Python_Hashcatshell/)

- [Python 天融信报告HTML转Excel](http://ssjt21.github.io/2017/11/Python_HtmltoExcel/)

<br>

转载请注明：[随时静听的博客](http://ssjt21.github.io) » [点击阅读原文](https://ssjt21.github.io/2017/11/Python_TK_Button/)