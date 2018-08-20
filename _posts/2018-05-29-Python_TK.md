--- 
layout: post
title: "Tkinter Scrollbar 滚动条控件"
date: 2018-05-28 08:13:06 
description: "Python Tkinter Scrollbar 滚动条控件使用"
tag: Tkinter
---

_This widget is used to implement scrolled listboxes, canvases, and text fields.The Scrollbar widget is almost always used in conjunction with a Listbox, Canvas, or Text widget. Horizontal scrollbars can also be used with the Entry widget._

**Scrollbar滚动条通常用于实现listbox,canvas,text文本框的滚动，也可以用于输入框的滚动设置，如果设置输入框的滚动只能设置x方向上的。**

### 滚动条使用方法：

1. 将Text,Canvas,Listbox控件的yscrollcommand(xscrollcommand)属性与Scrollbar控件的set方法绑定
2. 将Scrollbar控件的command属性与Text,Canvas,Listbox控件的yview或者xview方法绑定


### 创建垂直和水平滚动条

```python
master=Tk()

master.geometry('400x300')

text=Text(master,width=20,height=4)#创建Text控件
text.grid()

y_scroll=Scrollbar(master)
y_scroll.grid(row=0,column=1,sticky=N+S)#指定 上下展开
y_scroll.config(command=text.yview)

x_scroll=Scrollbar(master)
x_scroll.grid(row=1,sticky=W+E)#指定左右展开
x_scroll.config(command=text.xview)

text.config(yscrollcommand=y_scroll.set)
text.config(xscrollcommand=x_scroll.set)


y_scroll.config(orient=VERTICAL)#垂直显示，默认值是VERTICAL
x_scroll.config(orient=HORIZONTAL)#水平显示
master.mainloop()
```

**如果只是想创建垂直或者水平滚动条，请按照以上规则去掉其中一个即可。**


### 

```Python
# -*- coding: utf-8 -*-
from tkinter import *
root=Tk()
root.geometry("600x600")
#grid控件网格布局
#例子1
# sticky 指定文本的的位置 N,S,E,W
lab_1=Label(root,text="name").grid(row=0,sticky=W)
lab_2=Label(root,text="passwd").grid(row=1)
entry_1=Entry(root)
entry_2=Entry(root)
entry_1.grid(row=0,column=1)
entry_2.grid(row=1,column=1)

# 例子2
# columnspan
# rowspan
lab_3=Label(root,text="hello")
lab_4=Label(root,text="hi")
lab_3.grid(sticky=E)
lab_4.grid(sticky=E)
entry_3=Entry(root)
entry_4=Entry(root)
entry_3.grid(row=2,column=1)
entry_4.grid(row=3,column=1)
check_btn=Checkbutton(root,text='例子2')
check_btn.grid(columnspan=2,sticky=W)
img=PhotoImage(file="img.gif")
lab_5=Label(root,image=img)
lab_5.grid(row=2,column=2,columnspan=2,rowspan=2,sticky=W+E+N+S,padx=5,pady=5)
# 指定最小的列宽
root.columnconfigure(0,minsize = 100)
root.mainloop()
```
<img src="/images/posts/Python/Tkinter/Grid/Tkinter_Grid_1.jpg" >


推荐阅读：

- [Tkinter Button控件使用-2](https://ssjt21.github.io/2017/11/Python_TK_Button/)

- [Tkinter Canvas控件使用-3](https://ssjt21.github.io/2017/11/Python_TK_Canvas/)

- [Tkinter Label控件使用-5](https://ssjt21.github.io/2018/05/Python_TK_Label/)

- [Tkinter Entry输入框控件-6](https://ssjt21.github.io/2018/05/Python_TK_Entry/)

- [Tkinter Scrollbar滚动条控件-7](https://ssjt21.github.io/2018/05/Python_TK_Scrollbar/)

- [Python PIL Image类使用](http://ssjt21.github.io/2017/11/Python_PIL_Image_Module/)

- [Python调用Hashcat跑主机密码文件](http://ssjt21.github.io/2017/11/Python_Hashcatshell/)

- [Python pyexcel-xls使用对Excel进行读写操作](https://ssjt21.github.io/2018/01/Python_Pyexcel-xls/)


<br>

转载请注明：[随时静听的博客](http://ssjt21.github.io) » [点击阅读原文](https://ssjt21.github.io/2018/05/Python_TK_Scrollbar/)