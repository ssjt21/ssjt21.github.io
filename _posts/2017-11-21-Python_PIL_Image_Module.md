--- 
layout: post
title: "Python PIL Image Module"
date: 2017-11-21 13:13:06 
description: "Python PIL 图片处理 Image类"
tag: Python
---

### 打开，旋转并显示图片 - open() - rotate() - show()


- open(img_name),图片名字或者是文件对象(以rb打开方式的fp)

- rotate(degree_num),对图片进行旋转，参数为旋转的度数

- show(),展示打开的图片

- 以上函数的返回类型都是Image Object

```Python
from PIL import Image
im=open('demo.jpg')
im.rotate(45).show()    #图片旋转45°并显示
```

### 获取图片的信息 

- filename,图面名字，必须是以Image.open()方式打开，且当传入的参数是文件对象时，返回的是空字符串

- format,获取图片的格式，比如JPEG,GIF,

- mode,图片使用的存储格式,比如RGB(真彩),L(8-bit pixels,),1(1-bit pixels) 详细参见 [Mode value](http://pillow.readthedocs.io/en/latest/handbook/concepts.html#concept-modes)

- size,返回图片的尺寸,返回一个元组(width,height) 表示图片的宽和高

- width,height,图片的宽和高，返回类型为int

```Python
from PIL import Image
im=Image.open('demo.jpg')
print im.filename #输出图片的名字，im必须是open()函数打开的对象，并且非文件对象打开的方式
fp=open('demo.jpg','rb') #以只读二进制方式打开图片
im2=Image.open(fp)      #使用文件对象打开图片
print im2.filename #输出空的字符串

print im.format  #输出文件的格式

print im.mode   #输出图片使用的像素模式

print im.size   #输出图片的宽和高(width,height)

print im.width,img.height  #输出的图片的宽和高

```

### 图像通道融合

- alpha_composite(img1,img2),img1和img2的**mode**必须是**'RGBA'**,并且**size**要相同

- blend(img1,img2,alpha),对两张的图片**mode**没有做限制,但是**size**必须相同,融合公式为：`outImg=img1*(1.0-alpha)+img2*alpha`

```Python
from PIL import Image
img1=Image.open('demo.jpg')
img2=Image.open('demo2.jpg')
img3=Image.blend(img1,img2,0.2)
img3.show()
```
*图片1:demo.jpg*

<img src="/images/posts/Python/PIL/demo.jpg" height="500" width="800">

*图片2:demo2.jpg*

<img src="/images/posts/Python/PIL/demo.jpg" height="500" width="800">

*合成图片3*

<img src="/images/posts/Python/PIL/blend.jpg" height="500" width="800">


### 创建缩略图 - thumbnail()

```Python


```

















2017-11-21-Python_PIL_Image_Module


推荐阅读：

- [Python调用Hashcat跑主机密码文件](http://ssjt21.github.io/2017/11/Python_Hashcatshell/)

- [Python 天融信报告HTML转Excel](http://ssjt21.github.io/2017/11/Python_HtmltoExcel/)

<br>

转载请注明：[随时静听的博客](http://ssjt21.github.io) » [点击阅读原文](https://ssjt21.github.io/2017/11/Python_PIL_Image_Module/)