--- 
layout: post
title: "Tkinter Label使用-5"
date: 2018-5-27 10:13:06 
description: "Python Tkinter Label使用例子"
tag: Tkinter
---

### Label 标签

_To use a label, you just have to specify what to display in it (this can be text, a bitmap, or an image).Labels can display multiple lines of text.The label can only display text in a single font, but the text may span more than one line. In addition, one of the characters can be underlined, for example to mark a keyboard shortcut._

__label标签可以用来显示单行或多行的文本，字体类型只能是同一种，如果你想在一个Label标签内使用两种字体的话，是不被允许的，但是可以对字体加上下划线和快捷键（见事件）。除此之外Label控件还可以显示图片和位图。__

### first demo

```python
from Tkinter import *
master=Tk()# 实例化Tk()，创建顶级窗口
#在master顶级窗口创建Label控件，并设置显示文本为Hello world!
w=Label(master,text="Hello,world!")
w.pack()#显示Label控件
master.mainloop()#进入消息循环
```

<img src="/images/posts/Python/Tkinter/Label/label-1.jpg" >

### 设置Label的宽和高 width | height

```python
from Tkinter import *
master=Tk()# 实例化Tk()，创建顶级窗口
#在master顶级窗口创建Label控件，并设置显示文本为Hello world!
w=Label(master,text="Hello,world!",width=20,height=5)
w.pack()#显示Label控件
master.mainloop()#进入消息循环
```

_width和height单位说明：_
- 文本： 按照单一字体为单位
- 图片、位图：按照像素为单位

<img src="/images/posts/Python/Tkinter/Label/label-2.jpg" >

### 背景色（background|bg）、前景色(foreground|fg)、字体设置(font)

- 背景颜色设置：background="red" 或者 bg="red"
- 前景颜色设置（字体颜色）：foreground="red" 或者 fg="red"
- 字体设置： font=('Courier New',16,'bold italic'),指定字体为Courier New，字体的大小为16,字体样式bold italic 或者使用font='Courier\ New 16 bold italic'进行设置,其中的\是用来转义空格的

```PYTHON
from Tkinter import *
master=Tk()# 实例化Tk()，创建顶级窗口
w=Label(master,text="Hello,world!",width=20,height=5,bg='black',fg='white',font=('Courier New',16))
w.pack()#显示Label控件
master.mainloop()#进入消息循环
```

<img src="/images/posts/Python/Tkinter/Label/label-3-font-bg-fg.jpg" >

###  label文本位置设置 wraplenght、justify、anchor

- wraplength：用于设置一行文本显示的多少(用于多行文本的设置)，这个计算跟字体的大小有关系，比如字体大小为16，当设置wraplength=64时，也就是每行显示64/16=4个字体

通常情况下，用到wraplenth设置多行文本显示后也会设置多行文本的显示方式，就会用到anchor 和 justify两个属性：
- justify:指定多行文本的对齐方式，可以时left、right、center，默认值为center(justify='center')

__说明： justify的值也可以是LEFT、RIGHT、CENTER，但是使用的时候，必须是justify=LEFT，这区别于上面的justify='left'方式，一个是加入引号一个不加。两种方式显示的效果是一样的，选择哪一个都是可以。__

```python
from Tkinter import *

master=Tk()# 实例化Tk()，创建顶级窗口
w=Label(master,text="Helpo,world!",bg='black',fg='white',font='Courier\ New 16 bold italic',wraplength=100,justify='right')
w.pack()#显示Label控件
master.mainloop()#进入消息循环
```
<img src="/images/posts/Python/Tkinter/Label/label-4-wraplength-justify.jpg" >
- anchor: 设置文本在Label上的位置，有以下值可选

__N(north)、S(south)、W(west),e(east)和NE,NW,SE,SW,CENTER，默认值是CENTER。当设置标签的长宽比较大的时候，可以明显的看出anchor对文本显示位置的设置。__

```python
from Tkinter import *
master=Tk()# 实例化Tk()，创建顶级窗口
w=Label(master,text="Helpo,world!",width=40,height=6,bg='black',fg='white',font='Courier\ New 16 bold italic',wraplength=100,justify='right',anchor=E)
w.pack()#显示Label控件
master.mainloop()#进入消息循环
```

<img src="/images/posts/Python/Tkinter/Label/label-5-anchor.jpg" >



### 对Label标签绑定变量 StringVar()，textvariable

_在Tkinter中，很多控件都可以支持变量的绑定，使用变量绑定的好处是后期可以根据需要获取和修改控件中值。_

- 创建StringVar()变量：v=StringVar()
- 跟控件进行绑定：设置控件属性textvariable为v，textvariable=v
- 获取控件中绑定变量中的值：v.get()
- 设置控件中绑定变量中的值：v.set("hello")

```python
master=Tk()
v=StringVar()
lab=Label(master,width=60,height=10,textvariable=v)
lab.pack()
v.set('Hello,lqy')#设置控件中显示的值
print(v.get())#在控制台输出获取的值
master.mainloop()
```

<img src="/images/posts/Python/Tkinter/Label/label-6-stringvar.jpg" >

### Label 显示图片 image

_You can use the label to display PhotoImage and BitmapImage objects._

__详细的使用方式请参见教程PhotoImage和BitmapImage的使用__

__请确保已经安装PIL或者Pillow图片模块。下面使用的是PIL模块，PIL不支持Pyhton3.x，在Python3.x版本中你可以使用Pillow模块解决图片的显示问题。一定注意图片的格式问题，比如gif,JPEG等。__

```python
from Tkinter import *
from PIL import Image,ImageTk
master=Tk()
img=Image.open('ssjt.jpg')#打开一个图片对象
photo=ImageTk.PhotoImage(img)#转成TK IMG对象
lab=Label(master,image=photo)#指定image属性用于显示图爿
lab.image=photo#防止局部变量被销毁，进行持久化保存图片对象--这里很重要
lab.pack()
master.mainloop()
```

__注意： 一定不要更改导入PIL和Tkinter的顺序，否则会出错，如果你一定要更改导入顺序，请使用导入包名，然后通过（包名.方法()）的方式来用。__

- Note: When a PhotoImage object is garbage-collected by Python (e.g. when you return from a function which stored an image in a local variable), the image is cleared even if it’s being displayed by a Tkinter widget.

- To avoid this, the program must keep an extra reference to the image object. A simple way to do this is to assign the image to a widget attribute, like this:

-------
```python
    label = Label(image=photo)
    label.image = photo # keep a reference!
    label.pack()
```
-----

<img src="/images/posts/Python/Tkinter/Label/label-7-image.jpg" >

### Label 内边距(padx|pady)设置

- padx：设置水平方向上的内边距，默认值为1像素
- pady：设置垂直方向上的内边距，默认值为1像素

```python
from Tkinter import  *
master =Tk()
lab_pad=Label(master,bg='green',text='padx,pady设置',underline=2,padx=40,pady=20)
lab_pad.pack()
master.mainloop()
```

__其中underline设置文本下划线，默认值为-1标识没有.如果设置了值为1，标识对text中的字符的第二个加入下划线。__

<img src="/images/posts/Python/Tkinter/Label/label-8-pad.jpg" >

### Laber边框样式设置 (borderwidth,relief)

- borderwidth/bg:边框大小设置，默认值跟系统有关，一般是1px或者2px，使用bg=1或者boderwidth=1来设置
- relief：设置边框的显示样式，默认值为FLAT,其他值有SUNKEN, RAISED, GROOVE, and RIDGE. 

```python
from Tkinter import  *
master =Tk()
lab_1=Label(master,text='relief=SUNKEN设置',relief=SUNKEN,padx=40,pady=20)
lab_1.grid()
lab_2=Label(master,text='relief=RAISED',relief=RAISED,padx=40,pady=20)
lab_2.grid(row=1,column=1)
lab_3=Label(master,text='relief=GROOVE',relief=GROOVE,padx=40,pady=20)
lab_3.grid(row=2,column=0)
lab_4=Label(master,text='relief=RIDGE',relief=RIDGE,padx=40,pady=20)
lab_4.grid(row=3,column=2)

master.mainloop()
```

<img src="/images/posts/Python/Tkinter/Label/label-9-relief.jpg" >

### 图片和文本同时显示的方式compound

- 默认值为None,当存在图片时，图片覆盖文本
- CENTER:text显示在image上
- BOTTOM、LEFT,RIGHT、TOP:分别将文本显示在图片的下、左、右、上

```python
from Tkinter import *
from PIL import Image,ImageTk
master=Tk()
img=Image.open('ssjt.jpg')#打开一个图片对象
photo=ImageTk.PhotoImage(img)#转成TK IMG对象
lab=Label(master,text="你好",image=photo,fg='yellow',font=('Courier New',16,'bold'),compound=CENTER)#指定image属性用于显示图爿
lab.image=photo#防止局部变量被销毁，进行持久化保存图片对象
lab.pack()
master.mainloop()
```

<img src="/images/posts/Python/Tkinter/Label/label-10-compound.jpg" >

### 除以上外观还有其他不太常用的属性设置：


|属性|值|说明|
| - | :- | :- |
|activebackground|颜色值|设置激活状态下的背景色|
|activeforeground|颜色值|设置激活状态下的前景色|
|cursor|见文章底部|设置光标移动到label上的样式|
|disabledforeground|颜色值|当label被禁用时使用什么样的前景色|
|state|DISABLED,ACTIVE,NORMAL(default)|设置lable的状态|
|highlightbackground|颜色值|设置label没有焦点时的边框的颜色|
|highlightcolor|颜色值|设置label获取焦点时的边框颜色|
|highlightthickness|默认值为0，数字|设置高亮显示边框的宽度|


### cursor光标的值：
```PYTHON
arrow 箭头
 
man 人
 
based_arrow_down 基础向上箭头 
 
middlebutton 中间按钮
 
based_arrow_up 基础向下箭头
 
mouse 鼠标
 
boat 船
 
pencil 铅笔
 
bogosity 虚假度
 
pirate 海盗
 
bottom_left_corner 左下角 
 
plus 加
 
bottom_right_corner 右下角 
 
question_arrow 问题箭头
 
bottom_side 最下边
 
right_ptr 右指针
 
bottom_tee T型底
 
right_side 最右边
 
box_spiral 方螺旋
 
right_tee T型右
 
center_ptr 中指针
 
rightbutton 右按钮
 
circle 圆
 
rtl_logo rtl_logo
 
clock 表
 
sailboat 帆船
 
coffee_mug 咖啡杯
 
sb_down_arrow 宽下箭头
 
cross 十字
 
sb_h_double_arrow 宽水平双箭头 
 
cross_reverse 米字
 
sb_left_arrow 宽左箭头
 
crosshair 十字线
 
sb_right_arrow 宽右箭头
 
diamond_cross 十字钻
 
sb_up_arrow 宽上箭头
 
dot 点
 
sb_v_double_arrow 宽垂直双箭头 
 
dotbox 方点
 
shuttle 梭子型
 
double_arrow 双箭头
 
sizing 改变大小
 
draft_large 大拖拽
 
spider 蜘蛛
 
draft_small 小拖拽
 
spraycan 喷枪
 
draped_box 褶皱盒子
 
star 星星
 
exchange 交换
 
target 目标
 
fleur 十字花
 
tcross T型十字
 
gobbler 火鸡
 
top_left_arrow 左上箭头
 
gumby gumby（卡通角色）
 
top_left_corner左上角 
 
hand1 手型1
 
top_right_corner 
 
hand2 手型2
 
top_side 最上边
 
heart 心型
 
top_tee T型上
 
icon 图标
 
trek 跋涉
 
iron_cross 铁十字
 
ul_angle 左上角度
 
left_ptr 左指针
 
umbrella 雨伞
 
left_side 最左边
 
ur_angle 右上角度
 
left_tee T型左
 
watch 表
 
leftbutton
 
xterm 输入光标
 
ll_angle 左下角度
 
X_cursor X型指针
 
```



### Label 事件绑定 (bind)

__在Tkinter中几乎所有的控件都有事件(event)，一定要牢记lable是没有像Butto那样的command属性，因此label只能通过bind方法来绑定事件。详细的事件操作见bind事件绑定教程。__

- \<Button-1\> 表示鼠标左键
- \<Button-3\> 表示鼠标右键
- \<Buttom-2\> 表示鼠标中键

```python
from Tkinter import *
sign=False
def change_v(event):#第一个参数必须是event
    global sign
    if sign:
        v.set("has clicked me!")
        sign=False
    else:
        sign=True
        v.set("click me!")
master= Tk()
master.geometry('200x100')
v=StringVar()
lab=Label(master,textvariable=v)
v.set("click me")
lab.bind('<Button-1>',change_v)#绑定事件
lab.pack()
master.mainloop()

```
<img src="/images/posts/Python/Tkinter/Lable/label-11-bind.gif" >


推荐阅读：

- [Tkinter Button控件使用-2](https://ssjt21.github.io/2017/11/Python_TK_Button/)

- [Tkinter Canvas控件使用-3](https://ssjt21.github.io/2017/11/Python_TK_Canvas/)

- [Tkinter Entry输入框控件-6](https://ssjt21.github.io/2018/05/Python_TK_Entry/)

- [Python PIL Image类使用](http://ssjt21.github.io/2017/11/Python_PIL_Image_Module/)

- [Python调用Hashcat跑主机密码文件](http://ssjt21.github.io/2017/11/Python_Hashcatshell/)

- [Python pyexcel-xls使用对Excel进行读写操作](https://ssjt21.github.io/2018/1/Python_Pyexcel-xls/)


<br>

转载请注明：[随时静听的博客](http://ssjt21.github.io) » [点击阅读原文](https://ssjt21.github.io/2018/05/Python_TK_Label/)