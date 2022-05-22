

### 项目进展

5.21 开始 查询资料

5.22 摆烂   

界面设计  使用Qt designer设计大概布局,基本使用horizontal layout和vertical layout.

form layout经本人实验效果理想,不建议用作登陆界面. 

使用layout的目的,构建responsive的界面.一般前端会用这种说法.

即不同窗口大小不会导致应用界面出现鬼畜的情况.这里推荐b站某up主讲的课.个人觉得挺不错.

[白月黑羽编程的个人空间_哔哩哔哩_bilibili](https://space.bilibili.com/401981380)

大概效果

<img src="动画.gif" alt="动画" style="zoom:50%;" />



使用layout的几个注意点:

首先要了解sizepolicy

> SizePolicy的作用：
>
> A. Fixed：控件不能放大或者缩小，控件的大小就是它的sizeHint。
>
> B. Minimum：控件的sizeHint为控件的最小尺寸。控件不能小于这个sizeHint，但是可以
>
> 放大。
>
> C. Maximum：控件的sizeHint为控件的最大尺寸，控件不能放大，但是可以缩小到它的最小
>
> 的允许尺寸。
>
> D. Preferred：控件的sizeHint是它的sizeHint，但是可以放大或者缩小
>
> E. Expandint：控件可以自行增大或者缩小
>
> 注：sizeHint（布局管理中的控件默认尺寸，如果控件不在布局管理中就为无效的值）










### 记录项目中遇到的问题