--- 
layout: post
title: "Tkinter Canvas控件使用-3"
date: 2017-11-24 13:13:06 
description: "Python Tkinter Canvas按钮的使用例子"
tag: Tkinter
---

### Canvas 控件使用举例-1

```Python
# -*- coding: utf-8 -*-
from tkinter import *

root=Tk()
root.geometry("600x600")

# canvas控件使用
# 创建画布控件
cnv=Canvas(root,width=400,height=400)
cnv.configure(bg="white")#设置背景颜色为白色
cnv.grid(row=0,column=0)#显示画布控件

cnv.create_line(0,0,200,200)#画直线
# 画虚线，颜色为red
cnv.create_line(0,200,200,200,fill="red",dash=(1,10))
# 画矩形，填充颜色为green,bian框为red,边框宽6
cnv.create_rectangle(300,0,350,50,fill="green",outline="red",width=6)

# 删除画布上的所有内容
cnv.delete(ALL)

line=cnv.create_line(100,0,100,100,fill="red")
# 修改line坐标
cnv.coords(line,(0,0,50,50))
#修改line颜色
cnv.itemconfig(line,fill="blue")
#删除直线
cnv.delete(line)

# 画椭圆，矩形限制的椭圆
cnv.create_oval(50,50,100,100)

#画三角形
cnv.create_polygon(10,0,10,50,60,0)

# 画弧形 样式 开始的角度 偏移的角度
cnv.create_arc((10,10,100,100),style="pieslice",start=30,extent=30)

#画位图
bitmaps=["error", "gray75", "gray50", "gray25", "gray12", "hourglass", "info", "questhead", "question", "warning"]
for i,item in enumerate(bitmaps):
    cnv.create_bitmap((i+1)*30-10,150,bitmap=item)

#画图片
img=PhotoImage(file="demo.gif")
cnv.create_image(200,10,anchor=NW,image=img)

#画文本
cnv.create_text(300,300,text="SSJT",font=("Courier New", 14,"bold","underline"))


# 交互式绘画
def paint(event):
    color="#476042"
    x1,y1=(event.x-1),(event.y-1)
    x2,y2=(event.x+1),(event.y+1)
    cnv.create_oval(x1,y1,x2,y2,fill=color)
cnv.bind("<B1-Motion>",paint)

# 绘制组件
btn=Button(cnv,text="按钮")
cnv.create_window((100,50),window=btn,anchor=W)

root.mainloop()
```

<img src="/images/posts/Python/Tkinter/Canvas/Tkinter_Canvas_1.jpg" >

### Canvas item和事件绑定
```Python
from tkinter import *

root=Tk()
root.geometry("600x500")
# Canvas控件使用 2
cnv=Canvas(root,width=600,height=600)
cnv.configure(bg="white")#设置背景颜色为白色
cnv.grid(row=0,column=0)#显示画布控件

ret1=cnv.create_rectangle(10,10,110,110,width=8,tags=('r1','r2','r3'))

def printRect(event):
    print 'rectangle'

def printline(event):
    print 'line'
# # 绑定鼠标左键
# cnv.tag_bind('r1','<Button-1>',printRect)
# # 绑定鼠标右键
# cnv.tag_bind('r1','<Button-3>',printline)
# cnv.create_line(10,200,100,200,width=5,tags='r1')
# --------------
rt=cnv.create_rectangle(10,10,110,110,tags='r1')
print cnv.gettags(rt)
cnv.itemconfig(rt,tags=('r2','r3','r4'))
print cnv.gettags(rt)

cnv.create_rectangle(20,20,50,50,tags='r3')
for item in cnv.find_withtag('r3'):
    cnv.itemconfig(item,outline='blue')
print cnv.find_withtag('r4')

# rt上一个对象添加tag 'r6'
cnv.addtag_above('r6',rt)
# rt下一个对象添加tag 'r7'
cnv.addtag_below('r7',rt)

root.mainloop()
```




推荐阅读：

- [Tkinter Button控件使用-2](https://ssjt21.github.io/2017/11/Python_TK_Button/)

- [Python PIL Image类使用](http://ssjt21.github.io/2017/11/Python_PIL_Image_Module/)

- [Python调用Hashcat跑主机密码文件](http://ssjt21.github.io/2017/11/Python_Hashcatshell/)



<br>

转载请注明：[随时静听的博客](http://ssjt21.github.io) » [点击阅读原文](https://ssjt21.github.io/2017/11/Python_TK_Canvas/)