网上查到了一个比较好的[python自学文档](https://www.liaoxuefeng.com/wiki/1016959663602400)书写，可以点击去看下，里面对于基础的python相关知识讲解的很详细

下面开始正式的笔记记录

***

# python的安装

首先去官网下载[python解释器](https://www.python.org/downloads/)，我是直接下载的最新版

![image-20231104215702629](https://gitee.com/zhurui_alan/typora_image_store/raw/master/typora_images/image-20231104215702629.png)

下载完成之后，直接安装，记住安装过程中，要将add to path加上，安装完成之后一定要确认两个事情

> 1. 查看系统环境变量中path中是否含有已经安装的python解释器的python.exe所在的目录，如下图：
>
>    ![image-20231104215949657](https://gitee.com/zhurui_alan/typora_image_store/raw/master/typora_images/image-20231104215949657.png)
>
>    ![image-20231104220039275](https://gitee.com/zhurui_alan/typora_image_store/raw/master/typora_images/image-20231104220039275.png)
>
> 2. 确认打开系统命令行之后，输入下面这条命令，判断python成功添加了系统环境变量
>
>    ```bash
>    python --version
>    ```
>
>    如果安装+配置成功之后，会出现下面这张图：
>
>    ![image-20231104220259075](https://gitee.com/zhurui_alan/typora_image_store/raw/master/typora_images/image-20231104220259075.png)

# pycharm的安装

安装了python还不够，他其实只是一个编译器，真正想开发大型的项目，还需要我们开发工具IDE的支持，所以需要下载jetbrains的pycharm，这里我从[pycharm下载官网地址](https://www.jetbrains.com/zh-cn/pycharm/download/?section=windows)

这里记住安装的时候将该勾选的安装选项（比如这里add to path等都勾选上），安装成功之后得到下图![image-20231104220823678](https://gitee.com/zhurui_alan/typora_image_store/raw/master/typora_images/image-20231104220823678.png)

# python的输入和输出

常见的编程语言中都含有输入输出的这个概念，其实任何一个操作系统中都含有输入输出这个概念，python中也存在这个概念

![image-20231104223858896](https://gitee.com/zhurui_alan/typora_image_store/raw/master/typora_images/image-20231104223858896.png)

## 输入

input()函数，顾名思义，我们可以利用这个函数让用户输入一段字符串，然后针对这个数据去做自己想做的操作

![image-20231104224316565](https://gitee.com/zhurui_alan/typora_image_store/raw/master/typora_images/image-20231104224316565.png)

我们可以看到在python的input函数接口文档中，实现只有一个pass，感觉这里可能是外部封装了一个输入的接口，但是其实底层实现是用c语言实现的，通过看这个接口的注释，可以得出这里input是一个可以返回string类型的函数，但是前提是用户需要在命令行里面手动输入一些数据，当输入结束符（EOF）的时候，函数会结束命令行监听，返回输入的字符串数据，下面可以实现一下一段代码：

![image-20231104224642433](https://gitee.com/zhurui_alan/typora_image_store/raw/master/typora_images/image-20231104224642433.png)

<img src="https://gitee.com/zhurui_alan/typora_image_store/raw/master/typora_images/image-20231104224721491.png" alt="image-20231104224721491" style="zoom:50%;" />

## 输出

对于操作系统中另外一个常用的就是输出系统输出流，这里python也封装了一个接口，名为print()，其接口注释如下

![image-20231104224943351](https://gitee.com/zhurui_alan/typora_image_store/raw/master/typora_images/image-20231104224943351.png)

通过参数可以看出self为python接口中统一会包含的参数，表示其为当前这个对象的地址，args这个就是我们平时传入的要打印的字符串参数，sep为一个分割线，我们平时传参的时候可以传递多个参数，然后用逗号隔开，end表示当前最后一个值的结尾字符，默认为/n，file表示输出的流位置，如果我们不输入一个文件的地址的话，就默认调用系统默认输出流，即sys.stdout来进行输出

具体可以见下面这个例子：

![image-20231104225555360](https://gitee.com/zhurui_alan/typora_image_store/raw/master/typora_images/image-20231104225555360.png)

## 练习

这里针对输入输出的讲解已经结束，可以自己写一下下面的程序代码学习一下

> 请实现一个程序，实现乘法计算结果，要求让用户自己输入乘数、被乘数，然后输出这个运算式子，全程计算都由用户自己计算，我们只负责输出结果即可

```python
if __name__ == '__main__':
    param_1 = param_2 = result_value = 0
    while True:  # 使用无限循环
        param_1 = int(input("输入乘数："))  # 将输入的字符串转换为整数
        param_2 = int(input("输入被乘数："))
        print("请计算你刚才所出的这道题：", param_2, "*", param_1, "=")
        result_value = int(input())
        right_result_value = param_2 * param_1
        if (right_result_value == result_value):
            print("恭喜，答案正确！")  # 当答案正确时，跳出循环
            break
        else:
            print("抱歉，答案错误！")  # 当答案错误时，重新循环
    print("结果正确，你所计算的结果为：", param_2, "*", param_1, "=", result_value)
```

![image-20231104232203152](https://gitee.com/zhurui_alan/typora_image_store/raw/master/typora_images/image-20231104232203152.png)

![image-20231104232334696](https://gitee.com/zhurui_alan/typora_image_store/raw/master/typora_images/image-20231104232334696.png)