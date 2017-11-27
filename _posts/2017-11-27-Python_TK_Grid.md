--- 
layout: post
title: "Tkinter Grid网格布局使用-4"
date: 2017-11-27 10:13:06 
description: "Python Tkinter Grid网格布局的使用例子"
tag: Tkinter
---


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

- [Python PIL Image类使用](http://ssjt21.github.io/2017/11/Python_PIL_Image_Module/)

- [Python调用Hashcat跑主机密码文件](http://ssjt21.github.io/2017/11/Python_Hashcatshell/)



<br>

转载请注明：[随时静听的博客](http://ssjt21.github.io) » [点击阅读原文](https://ssjt21.github.io/2017/11/Python_TK_Grid/)