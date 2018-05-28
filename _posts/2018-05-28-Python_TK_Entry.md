--- 
layout: post
title: "Tkinter Entry输入框控件-6"
date: 2018-05-28 09:13:06 
description: "Python Tkinter Entry输入框控件使用"
tag: Tkinter
---


_The Entry widget is a standard Tkinter widget used to enter or display a single line of text._

__Entry控件是Tkinter中的文本输入控件，一般用于单行文本输入，如果需要多行文本的录入请选择Text控件。__



###  Entry使用例子

```python
e=Entry(master)#创建输入框实例
e.pack()#显示
e.delete(0,END)#删除输入框的值
e.insert(0,"Hello")#向输入框填入值
print(e.get())#获取输入框的值并在控制台打印
```
<img src="/images/posts/Python/Tkinter/Entry/entry-1-demo.jpg" >

### 以下属性请参见Label控件的使用

__以下所有列出来的属性都可以通过.config(** options)或者.configure(** options)来设置__


- bg,background:背景颜色设置
- fg,foreground:前景颜色设置，（字体颜色设置）
- bd,borderwidth:边框设置，使用单位是像素
- font:字体设置,font=(字体类型,字号,字体样式)
- justify:在在控件中的如何显示，可选值LEFT(default),RIGHT,CENTER
- relief:边框样式设置,可选值SUNKEN(default),RAISED,GROOVE,RIDGE
- state: 只当输入框的状态，可选值NORMAL(default),DISABLED(等价readonly),如果指定了readonly或者DISABLED,有关insert或者delete操作都将被忽略
- takefocus:是否可以使用Tab键来获取焦点，默认值True
- textvariable:指定绑定的变量实例，实例必须是StringVar类
- cursor:光标样式显示设置，参见Label控件

### Entry不常用属性参考

- exportselection:**不太懂**，If true, selected text is automatically exported to the clipboard. Default is true. (exportSelection/ExportSelection)
- insertwidth:设置插入光标的大小
- insertbackground:设置光标的背景色，只有设置insertwidth值比较大的时候才能看到效果，跟光标的with和光标样式有关
- insertborderwidth：插入时光标的边框大小，只有在设置了insertwidth值比较大的时候才能看到效果
- insertofftime:Together with insertontime, this option controls cursor blinking. Both values are given in milliseconds. 控制光标闪烁的事件，和insertontime一起使用
- insertontime:参见insertontime
- selectborderwidth:设置选中时的边框大小，单位像素
- highlightbackground:
Together with highlightcolor, this option controls how to draw the focus highlight border. This option is used when the widget doesn’t have focus. The default is system specific. 
- highlightcolor：
Same as highlightbackground, but is used when the widget has focus. (highlightColor/HighlightColor)
- highlightthickness：
The width of the focus highlight border. Default is typically a few pixels, unless the system indicates focus by modifying the button itself (like on Windows). 






### Entry的一些常用属性介绍

- selectbackground:设置输入框中的字符被选中时的背景颜色
- selectforeground:设置输入框中选中字符的字体颜色
- show:指定输入框中字符显示被什么字符替代，一般常用在密码输入的地方，show='*'，可以使用show=''还原默认的显示方式
- disabledbackground:设置state=DISABLED时的背景色
- disabledforeground:设置state=DISABLED时的字体颜色
- readonlybackground:设置成只读时控件的背景色
- validate:设置对输入框的值进行校验，请使用validatecommand指定一个自定义的函数对数据校验，返回结果为True或者False，请确保validate的值不是None,validate的可选值None(default),'focusin'(获取焦点时校验),'focusout'(失去焦点时进行校验),'key',送上一段官方解释：You can use “focus” to validate whenever the widget gets or loses the focus, “focusin” to validate only when it gets focus, “focusout” to validate when it loses focus, “key” on any modification, and ALL for all situations. Default is NONE (no validation). (validate/Validate)
- validatecommand,vcmd:指定校验使用的函数，请确保validate不是None
- xscrollcommand:设置水平滚动条，需要配合Scrollbar控件一起使用，请参见Scrollbar控件的使用

```python
master=Tk()
master.geometry('400x300+200+200')
def is_num():
    try:

        int(e.get())
        print(222)
        return True
    except:
        print(333)
        return False


scroll_bar=Scrollbar(master)
scroll_bar.grid(row=1)
e=Entry(master)
e.config(selectbackground='green')#设置选中后的背景色
e.config(selectforeground='red')#设置被选中后的字体颜色
e.config(show='*')#设置输入框中字符显示被*替代，一般常用在密码输入的地方
e.config(show='')#还原默认的显示方式
e.config(insertbackground='purple')
# e.config(state=DISABLED)
e.config(disabledbackground='yellow')
e.insert(0,'666')
# e.config(exportselection=False)
e.config(insertborderwidth=6)
e.config(insertwidth=30)
e.config(insertofftime=600)
e.config(insertontime=200)
e.config(selectborderwidth=66)
e.config(validate='focusout')
e.config(vcmd=is_num)
e.config(xscrollcommand=scroll_bar.set)
e.grid(row=0)
scroll_bar.config(command=e.xview)
master.mainloop()
```

### Entry绑定变量以及置的获取

- makeentry函数是自定义的函数，用于快速创建一个label和一个输入框，并可以通过master指定两者的父窗口，通过caption指定label的标签内容，通过width来设置输入框的宽度，通过可变关键字参数设置输入框的附加参数
- 创建一个按钮控件绑定鼠标左键，绑定事件login,在事件函数中判断用户名是否为空，是否正确
- 创建msg标签并绑定变量可以显示文本，用于提示登陆操作的提示
- 使用绑定变量的get()可以获取输入框的值
- 使用绑定变量的set()方法可以设置输入框的值


```python

def makeentry(master,caption,width=None,**options):
    Label(master,text=caption).pack(side=LEFT)
    entry=Entry(master,**options)
    if width:
        entry.config(width=width)
    entry.pack(side=LEFT)
    return entry

user_var=StringVar()
pass_var=StringVar()
user=makeentry(master,'用户名：',10,textvariable=user_var)
password=makeentry(master,"密码",10,show='*',textvariable=pass_var)#指定输入框显示为*模式
user_var.set("请输入用户名")

def login(event):
    global msg
    username=user.get()#获取输入框用户名的值
    password_val=password.get()#获取密码的值
    if not (username and password_val):#判断是否为空
        msg.set("用户名和密码不能为空！")
    elif username=='lqy' and password_val=='0925':
        msg.set('登陆成功！')
    else:
        msg.set('用户名或密码错误！')
btn=Button(master,text="登陆")#创建按钮v
btn.pack(side=LEFT)
btn.bind('<Button-1>',login)#绑定鼠标左键事件

msg=StringVar()
msg_label=Label(master,textvariable=msg).pack(side=LEFT)

```

<img src="/images/posts/Python/Tkinter/Entry/entry-2-demo2.gif" >


### Entry控件的方法

- delete(first,last=None)：删除first-last字符，包含first和last,删除所有字符delete(0,END)
- get():获取输入框的值
- icursor(index):设置光标到index的位置，还可以使用INSERT常量
- index(index)：获取指定位置的下标，比如INSERT,END等
- insert(index,string):在index处插入字符串，可以指定输入框的末尾即END，也可以指定输入框的开头部分添加，使用0
- scan_dragto(x):将光标快速移动到指定的坐标X的位置上，快速定位到输入框的开始 **不太懂**Sets the scanning anchor for fast horizontal scrolling to the given mouse coordinate.
- scan_mark(x):**不太懂** Scrolls the widget contents sideways according to the given mouse coordinate. The text is moved 10 times the distance between the scanning anchor and the new position.
- select_adjust(x):快速扩展选择到字符x的位置
- select_clear():清除所有选择
- select_from(index):**不太懂** Starts a new selection. This also sets the ANCHOR index.
- select_present:检测输入框是否有文本被选中，如果被选中返回True,否则返回False
- select_range(start,end):选中start-end字符，必须是end>start
- select_to(index):选中光标到给定字符的位置
- xview(index):查看给定位置的字符，一般配合scrollbar控件使用，可以制作滚动歌词显示
- xview_moveto(fraction)：**不太懂**Adjusts the entry view so that the given offset is at the left edge of the canvas. Offset 0.0 is the beginning of the entry string, 1.0 the end.
- xview_scroll(number, what)：**不太懂**Scrolls the entry view horizontally by the given amount.

```python
master=Tk()

master.geometry('300x200')



e=Entry(master,width=50)
e.grid()

def on_click_icursor2(event):#设置光标的位置
    e.icursor(2)#可以设置成END,INSERT,0等

def on_click_index2(event):
    print(e.index(INSERT))#获取光标的坐标

def on_click_insert(event):
    e.insert(END,'hello')#在输入框的末尾插入hello

def on_click_scan_dragto(event):#不太懂
    # e.scan_dragto(500)
    e.scan_mark(30)
    #将光标快速移动到第6个字符的位置上,当内容特别多的时候可以快速定位到开头或者指定的位置上

def on_click_scan_adjust(event):#
    e.select_adjust(2)#快熟扩展选择到下第二个字符

def on_click_scan_clear(event):#
    e.select_clear()#清除所有选择
def on_click_scan_from(event):#不懂
    e.select_from(ANCHOR)#

def on_click_scan_present(event):#
    print(e.select_present())#检测是否有文本被选中，如果被选中返回True,否者返回False

def on_click_select_range(event):#
    e.select_range(2,6)#选中第二个到第六个字符

def on_click_select_to(event):#
    e.select_to(6)#选中光标到给定位置之间的字符
i=0
def on_click_xview(event):#可以制作滚动歌词
    global  i
    e.xview(i)#查看给定坐标的字符
    i=i+2
def on_click_moveto(event):#不懂
    e.xview_moveto(0.5)
btn=Button(master,text='BTN')
btn.grid()
btn.bind('<Button-1>',on_click_icursor2)

btn.bind('<Button-1>',on_click_index2)

btn.bind('<Button-1>',on_click_insert)

btn.bind('<Button-1>',on_click_scan_dragto)
btn.bind('<Button-1>',on_click_scan_adjust)
btn.bind('<Button-1>',on_click_scan_clear)
btn.bind('<Button-1>',on_click_scan_from)
btn.bind('<Button-1>',on_click_scan_present)
btn.bind('<Button-1>',on_click_select_range)
btn.bind('<Button-1>',on_click_select_to)
btn.bind('<Button-1>',on_click_xview)
btn.bind('<Button-1>',on_click_moveto)
master.mainloop()
```





推荐阅读：

- [Tkinter Button控件使用-2](https://ssjt21.github.io/2017/11/Python_TK_Button/)

- [Tkinter Canvas控件使用-3](https://ssjt21.github.io/2017/11/Python_TK_Canvas/)

- [Tkinter Label控件使用-5](https://ssjt21.github.io/2018/05/Python_TK_Label/)

- [Tkinter Entry输入框控件-6](https://ssjt21.github.io/2018/05/Python_TK_Entry/)

- [Python PIL Image类使用](http://ssjt21.github.io/2017/11/Python_PIL_Image_Module/)

- [Python调用Hashcat跑主机密码文件](http://ssjt21.github.io/2017/11/Python_Hashcatshell/)

- [Python pyexcel-xls使用对Excel进行读写操作](https://ssjt21.github.io/2018/1/Python_Pyexcel-xls/)


<br>

转载请注明：[随时静听的博客](http://ssjt21.github.io) » [点击阅读原文](https://ssjt21.github.io/2018/05/Python_TK_Entry/)