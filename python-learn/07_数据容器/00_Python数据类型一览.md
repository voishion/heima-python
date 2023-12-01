## 一、Python基本数据类型一览

一般分为6种：数值（Numbers）、字符串（String）、列表（List）、元组（Tuple）、字典（Dictionary）、集合（Set）。
本文详细讲解Python中变量赋值、数据类型以及数据类型的转换。

### 1、变量赋值
- Python 中的变量赋值不需要类型声明。
- 每个变量在内存中创建，都包括变量的标识，名称和数据这些信息。
- 每个变量在使用前都必须赋值，变量赋值以后该变量才会被创建。
- 等号 = 用来给变量赋值。

```python
num = 100 # 赋值整型变量
weight = 100.0 # 浮点型
name = "ShowMeAI" # 字符串
 
print(num)
print(weight)
print(name)
```
以上实例中，100，100.0和"ShowMeAI"分别赋值给num，weight，name变量。
执行以上程序会输出如下结果：
```
100
100.0
ShowMeAI
```

### 2.多变量赋值

Python允许你同时为多个变量赋值。例如：
```python
a = b = c = 1
```
以上实例，创建一个整型对象，值为1，三个变量被分配到相同的内存空间上。

您也可以为多个对象指定多个变量。例如：
```python
a, b, c = 1, 2, "ShowMeAI"
```
以上实例，两个整型对象 1 和 2 分别分配给变量 a 和 b，字符串对象 "ShowMeAI" 分配给变量 c。

### 4.标准数据类型

Python 定义了一些标准类型，用于存储各种类型的数据。

Python有最常用的5个标准数据类型：

- Numbers（数值）
- String（字符串）
- List（列表）
- Tuple（元组）
- Dictionary（字典）

### 5.Numbers（数值）

数值数据类型用于存储数值。

他们是**不可改变的数据类型**，这意味着改变数字数据类型会分配一个新的对象。

Python支持四种不同的数字类型：

- int（有符号整型）

- float（浮点型）

- complex（复数）

![](https://ask.qcloudimg.com/http-save/yehe-8934644/008070f3f2ed4ee2264f436b2b93aaf4.png)

### 6.String（字符串）

字符串或串(String)是由数字、字母、下划线组成的一串字符。

一般记为 :

```python
s = "a1a2···an"   # n>=0
```

它是编程语言中表示文本的数据类型。

python的字串列表有2种取值顺序:

- 从左到右索引默认0开始的，最大范围是字符串长度少1
- 从右到左索引默认-1开始的，最大范围是字符串开头

![](https://ask.qcloudimg.com/http-save/yehe-8934644/29ed357d197306fb1fe1601d892ea6da.png)

如果你要实现从字符串中获取一段子字符串的话，可以使用 **头下标:尾下标** 来截取相应的字符串，其中下标是从 0 开始算起，可以是正数或负数，下标可以为空表示取到头或尾。

**头下标:尾下标** 获取的子字符串包含头下标的字符，但不包含尾下标的字符。

比如:

```python
>>> s = 'ShowMeAI'
>>> s[6:8]
'AI'
```

当使用以冒号分隔的字符串，python 返回一个新的对象，结果包含了以这对偏移标识的连续的内容，左边的开始是包含了下边界。

上面的结果包含了 **s1** 的值 b，而取到的最大范围不包括**尾下标**，就是 **s5** 的值 f。

可以使用**加号（+）**对字符串进行连接，使用**星号（\*）**对字符串进行重复操作。如下（以下代码可以在[在线python3环境](https://cloud.tencent.com/developer/tools/blog-entry?target=http%3A%2F%2Fblog.showmeai.tech%2Fpython3-compiler%2F&source=article&objectId=1945472)中运行）：

```python
str = 'Hello ShowMeAI!'
 
print(str) # 输出完整字符串
print(str[0]) # 输出字符串中的第一个字符
print(str[2:5]) # 输出字符串中第三个至第六个之间的字符串
print(str[2:]) # 输出从第三个字符开始的字符串
print(str * 2) # 输出字符串两次
print(str + " Awesome") # 输出连接的字符串
```

以上实例输出结果：

```js
Hello ShowMeAI!
H
llo
llo ShowMeAI!
Hello ShowMeAI!Hello ShowMeAI!
Hello ShowMeAI! Awesome
```

Python 列表截取可以接收第三个参数，参数作用是截取的步长，以下实例在索引 1 到索引 4 的位置并设置为步长为 2（间隔一个位置）来截取字符串：

![](https://ask.qcloudimg.com/http-save/yehe-8934644/19b23056b82637f83077b87670056688.png)

### 7.List（列表）

List（列表） 是 Python 中使用最频繁的数据类型。

列表可以完成大多数集合类的数据结构实现。它支持字符，数字，字符串甚至可以包含列表（即嵌套）。

列表用`[]`标识，是 python 最通用的复合数据类型。

列表中值的切割也可以用到变量 **头下标:尾下标** ，就可以截取相应的列表，从左到右索引默认 0 开始，从右到左索引默认 -1 开始，下标可以为空表示取到头或尾。

![](https://ask.qcloudimg.com/http-save/yehe-8934644/05cc7e7a09afefeea0b85782fae82304.png)

![](https://ask.qcloudimg.com/http-save/yehe-8934644/3363b74d5ac44bc6006610313a3d1185.png)

加号 **+** 是列表连接运算符，星号 ***** 是重复操作。如下（以下代码可以在[在线python3环境](https://cloud.tencent.com/developer/tools/blog-entry?target=http%3A%2F%2Fblog.showmeai.tech%2Fpython3-compiler%2F&source=article&objectId=1945472)中运行）：

```python
list = [ 'ShowMeAI', 786 , 2.23, 'show', 70.2 ]
tinylist = [123, 'show']
 
print(list) # 输出完整列表
print(list[0]) # 输出列表的第一个元素
print(list[1:3]) # 输出第二个至第三个元素 
print(list[2:]) # 输出从第三个开始至列表末尾的所有元素
print(tinylist * 2) # 输出列表两次
print(list + tinylist) # 打印组合的列表
```

以上实例输出结果：

```
['ShowMeAI', 786, 2.23, 'show', 70.2]
ShowMeAI
[786, 2.23]
[2.23, 'show', 70.2]
[123, 'show', 123, 'show']
['ShowMeAI', 786, 2.23, 'show', 70.2, 123, 'show']
```

更多python列表的详细讲解知识可以参考[python列表](https://cloud.tencent.com/developer/tools/blog-entry?target=http%3A%2F%2Fshowmeai.tech%2Farticle-detail%2F77&source=article&objectId=1945472)

### 8.Tuple（元组）

元组是另一个数据类型，类似于 List（列表）。

![](https://ask.qcloudimg.com/http-save/yehe-8934644/99cffe94ff7e14545e32f52047e9107c.png)

元组用 **()** 标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。（以下代码可以在[在线python3环境](https://cloud.tencent.com/developer/tools/blog-entry?target=http%3A%2F%2Fblog.showmeai.tech%2Fpython3-compiler%2F&source=article&objectId=1945472)中运行）

```python
tuple = ( 'ShowMeAI', 786 , 2.23, 'show', 70.2 )
tinytuple = (123, 'show')
 
print(tuple) # 输出完整元组
print(tuple[0]) # 输出元组的第一个元素
print(tuple[1:3]) # 输出第二个至第四个（不包含）的元素 
print(tuple[2:]) # 输出从第三个开始至列表末尾的所有元素
print(tinytuple * 2) # 输出元组两次
print(tuple + tinytuple) # 打印组合的元组
```

以上实例输出结果：

```
('ShowMeAI', 786, 2.23, 'show', 70.2)
ShowMeAI
(786, 2.23)
(2.23, 'show', 70.2)
(123, 'show', 123, 'show')
('ShowMeAI', 786, 2.23, 'show', 70.2, 123, 'show')
```

以下是元组无效的，因为元组是不允许更新的。而列表是允许更新的：

```python
tuple = ( 'ShowMeAI', 345 , 2.23, 'show', 456.2 )
list = [ 'ShowMeAI', 345 , 2.23, 'show', 456.2 ]
tuple[2] = 100    # 元组中是非法应用
list[2] = 100     # 列表中是合法应用
```

更多python元组的详细讲解知识可以参考[python元组](https://cloud.tencent.com/developer/tools/blog-entry?target=http%3A%2F%2Fshowmeai.tech%2Farticle-detail%2F78&source=article&objectId=1945472)

### 9.Dictionary（字典）

字典(dictionary)是除列表以外python之中最灵活的内置数据结构类型。列表是有序的对象集合，字典是无序的对象集合。

两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。

![](https://ask.qcloudimg.com/http-save/yehe-8934644/0eab18ad68587c35e75cacafe353fd7c.png)

字典用"{ }"标识。字典由索引(key)和它对应的值value组成。（以下代码可以在[在线python3环境](https://cloud.tencent.com/developer/tools/blog-entry?target=http%3A%2F%2Fblog.showmeai.tech%2Fpython3-compiler%2F&source=article&objectId=1945472)中运行）

```python
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
 
tinydict = {'name': 'ShowMeAI','code':3456, 'dept': 'AI'}
 
print(dict['one']) # 输出键为'one' 的值
print(dict[2]) # 输出键为 2 的值
print(tinydict) # 输出完整的字典
print(tinydict.keys()) # 输出所有键
print(tinydict.values()) # 输出所有值
```

输出结果为：

```
This is one
This is two
{'name': 'ShowMeAI', 'code': 3456, 'dept': 'AI'}
dict_keys(['name', 'code', 'dept'])
dict_values(['ShowMeAI', 3456, 'AI'])
```

更多python字典的详细讲解知识可以参考[python字典](https://cloud.tencent.com/developer/tools/blog-entry?target=http%3A%2F%2Fshowmeai.tech%2Farticle-detail%2F79&source=article&objectId=1945472)

### 10.Set（集合）

集合（Set）是一个无序的不重复元素序列。

可以使用大括号 **{ }** 或者 **set()** 函数创建集合，注意：创建一个空集合必须用 **set()** 而不是 **{ }**，因为 **{ }** 是用来创建一个空字典。

![](https://img-blog.csdnimg.cn/49e54a7797a24b5ea563483057583da0.png)

创建格式：

```python
param = {1, 2}
param = set('A','B')
```

如下为示例代码（代码可以在[在线python3环境](http://blog.showmeai.tech/python3-compiler/)中运行）：

```python
company = {'Baidu', 'ShowMeAI', 'google', 'ByteDance', 'ShowMeAI', 'Taobao', 'Tencent'}

# 这里演示的是去重功能
print(company)
>>>{'Baidu', 'ShowMeAI', 'google', 'ByteDance', 'Taobao', 'Tencent'}

# 快速判断元素是否在集合内
print('Baidu' in company)         
>>>True
```

类似列表推导式，同样集合支持集合推导式(Set comprehension)：

```python
a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)
>>>{'r', 'd'}
```

#### 集合的基本操作

![](https://img-blog.csdnimg.cn/1a772a69859645dcb12bdff6aaacafe1.png)

![](https://img-blog.csdnimg.cn/9474374fdfb0449893228fef038e7c8e.png)



### 11.Python数据类型转换

有时候，我们需要对数据内置的类型进行转换，数据类型的转换，你只需要将数据类型作为函数名即可。

以下几个内置的函数可以执行数据类型之间的转换。这些函数返回一个新的对象，表示转换的值。

| 函数                | 描述                                                |
| :------------------ | :-------------------------------------------------- |
| int(x ,base)        | 将x转换为一个整数                                   |
| long(x ,base )      | 将x转换为一个长整数                                 |
| float(x)            | 将x转换到一个浮点数                                 |
| complex(real ,imag) | 创建一个复数                                        |
| str(x)              | 将对象 x 转换为字符串                               |
| repr(x)             | 将对象 x 转换为表达式字符串                         |
| eval(str)           | 用来计算在字符串中的有效Python表达式,并返回一个对象 |
| tuple(s)            | 将序列 s 转换为一个元组                             |
| list(s)             | 将序列 s 转换为一个列表                             |
| set(s)              | 转换为可变集合                                      |
| dict(d)             | 创建一个字典。d 必须是一个序列 (key,value)元组。    |
| frozenset(s)        | 转换为不可变集合                                    |
| chr(x)              | 将一个整数转换为一个字符                            |
| unichr(x)           | 将一个整数转换为Unicode字符                         |
| ord(x)              | 将一个字符转换为它的整数值                          |
| hex(x)              | 将一个整数转换为一个十六进制字符串                  |
| oct(x)              | 将一个整数转换为一个八进制字符串                    |

## 二、可变和不可变数据类型

### 1.区别

**可变数据类型**：当该数据类型对应的变量的值发生了变化时，如果它对应的内存地址不发生改变，那么这个数据类型就是可变数据类型。

**不可变数据类型**：当该数据类型对应的变量的值发生了变化时，如果它对应的内存地址发生了改变，那么这个数据类型就是不可变数据类型。

**总结：可变数据类型更改值后，内存地址不发生改变；不可变数据类型更改值后，内存地址发生改变。**

### 2.不可变数据类型

> 不可变数据类型：数值类型（int、float、bool）、string（字符串）、tuple（元组）、frozenset（不可变集合）

### 3.可变数据类型

> 可变数据类型：list（列表）、dict（字典）

## 三、序列类型的分类

- 容器序列

  > list、tuple、deque

- 扁平序列

  > str、bytes、bytearray、array

- 可变序列

  > list、deque、bytearray、array

- 不可变序列

  > str、bytes、tuple


## END、要点速查版

[ShowMeAI](https://www.showmeai.tech/)图解Python编程系列推荐

- [ShowMeAI 图解 Python 编程(1) | 介绍](https://www.showmeai.tech/article-detail/61)
- [ShowMeAI 图解 Python 编程(2) | 安装与环境配置](https://www.showmeai.tech/article-detail/65)
- [ShowMeAI 图解 Python 编程(3) | 基础语法](https://www.showmeai.tech/article-detail/66)
- [ShowMeAI 图解 Python 编程(4) | 基础数据类型](https://www.showmeai.tech/article-detail/67)
- [ShowMeAI 图解 Python 编程(5) | 运算符](https://www.showmeai.tech/article-detail/68)
- [ShowMeAI 图解 Python 编程(6) | 条件控制与if语句](https://www.showmeai.tech/article-detail/69)
- [ShowMeAI 图解 Python 编程(7) | 循环语句](https://www.showmeai.tech/article-detail/70)
- [ShowMeAI 图解 Python 编程(8) | while循环](https://www.showmeai.tech/article-detail/71)
- [ShowMeAI 图解 Python 编程(9) | for循环](https://www.showmeai.tech/article-detail/72)
- [ShowMeAI 图解 Python 编程(10) | break语句](https://www.showmeai.tech/article-detail/73)
- [ShowMeAI 图解 Python 编程(11) | continue语句](https://www.showmeai.tech/article-detail/74)
- [ShowMeAI 图解 Python 编程(12) | pass语句](https://www.showmeai.tech/article-detail/75)
- [ShowMeAI 图解 Python 编程(13) | 字符串及操作](https://www.showmeai.tech/article-detail/76)
- [ShowMeAI 图解 Python 编程(14) | 列表](https://www.showmeai.tech/article-detail/77)
- [ShowMeAI 图解 Python 编程(15) | 元组](https://www.showmeai.tech/article-detail/78)
- [ShowMeAI 图解 Python 编程(16) | 字典](https://www.showmeai.tech/article-detail/79)
- [ShowMeAI 图解 Python 编程(17) | 集合](https://www.showmeai.tech/article-detail/80)
- [ShowMeAI 图解 Python 编程(18) | 函数](https://www.showmeai.tech/article-detail/81)
- [ShowMeAI 图解 Python 编程(19) | 迭代器与生成器](https://www.showmeai.tech/article-detail/82)
- [ShowMeAI 图解 Python 编程(20) | 数据结构](https://www.showmeai.tech/article-detail/83)
- [ShowMeAI 图解 Python 编程(21) | 模块](https://www.showmeai.tech/article-detail/84)
- [ShowMeAI 图解 Python 编程(22) | 文件读写](https://www.showmeai.tech/article-detail/85)
- [ShowMeAI 图解 Python 编程(23) | 文件与目录操作](https://www.showmeai.tech/article-detail/86)
- [ShowMeAI 图解 Python 编程(24) | 错误与异常处理](https://www.showmeai.tech/article-detail/87)
- [ShowMeAI 图解 Python 编程(25) | 面向对象编程](https://www.showmeai.tech/article-detail/88)
- [ShowMeAI 图解 Python 编程(26) | 命名空间与作用域](https://www.showmeai.tech/article-detail/89)
- [ShowMeAI 图解 Python 编程(27) | 时间和日期](https://www.showmeai.tech/article-detail/90)

