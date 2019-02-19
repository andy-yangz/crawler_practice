# Python 爬虫笔记

The Website is API.

## Requests

### Request

request(url, params, kwargs)->Response, Request

status_code (200成功, 404失败)

200的话就可以应用下面的

#### 异常

ConnectionError

HTTPError

URLRequired

TooManyRedirects

ConnectTimeout

Timeout

#### HTTP 协议

GET，HEAD，

POST，PUT，PATCH，DELETE

text, encoding （猜测）, apparent_encoding, content

### 网络爬虫

#### 尺寸

爬取网页，玩转网页。小规模，数据量小，爬取速度不敏感。Requests

爬取网站。中规模，数据规模大。Scrapy

爬取全网。大规模，搜索引擎，定制开发。

#### 限制

- 来源审查
- Robots协议：哪些
  - user-agent
  - disallow

Robots 怎么使用：自动识别robots.txt，然后爬取。类人行为可不参考robots。

get

head

post

put

patch

delete

### Robots

## Beutiful Soup

解析遍历维护“标签树”的功能库

### BeutifulSoup类

soup.a; soup.title; 这些是tag

有各种属性: name，attrs(字典), string,

### 遍历方法

.children, descendants

parent, parents

next_siblings

![1549971613832](C:\Users\surface\AppData\Roaming\Typora\typora-user-images\1549971613832.png)

### 信息标记和提取方法

信息与标记：增加信息维度，可用于通讯存储，程序理解

xml <name></name> <name /> <!-- -->

json: key:value 有类型键值对

YAML 无类型键值对。缩进表达所属关系。- 表并列。| 表整块数据。# 表注释

#### 比较

XML：最早，扩展性好，繁琐

json：有类型适合程序处理，简洁

yaml：无类型，信息比例高，可读性好

#### 查找方法

- 解析标记形式
- 搜索
- 结合

#### find_all

name，attrs，recursive，string（对字符串检索），

### 实战



## Re 正则表达式

用于提取页面关键信息，用来简洁表达一组字符串。

通用的字符串表达框架。“简洁”和“特征”

编译：将符合语法的字符串转换成特征

### 语法

字符 + 操作符

#### 操作符

. 任何单个字符

[] 字符集 [^] 非

*零或无限次 + 1或无限次 ？0或1次

| 左右表达式任意

{m} 扩展m到n次

^ 匹配开头，$ 匹配结尾

（）分组标记 \d 数字 \w 单词字符(A-Za-z0-9_)

#### 经典表达式

^[A-Za-z]+$ 26个字母字符串

^[A-Za-z0-9]+$

^-?\d+$ 整数

^[0-9]\*\[1-9][0-9]\*$ 

[\u4e00-\u9fa5]

### re

import re

raw string不包含再转义。当包含转义符时，用raw string

re.search match findall split finditer sub

regex 也都可以使用

#### match 对象

string, re, pos, endpos

group(0), start(), end()

贪婪匹配，最小匹配（操作符后加？变为最小匹配）

## Scrapy

爬虫框架，实现爬虫功能的软件结构和功能组件集合。

![1550489558143](C:\Users\surface\AppData\Roaming\Typora\typora-user-images\1550489558143.png)

1. 爬取请求
2. 请求转发scheduler，调度
3. engine获得下个爬取请求
4. 发送给Downloader
5. 爬取后响应给Engine
6. 响应发送给Spider
7. 处理响应，获得爬取Item和Request
8. Item给框架出口Item Pipeline
9. Request 给Scheduler

#### Engine

- 控制模块数据流
- 根据条件触发事件

#### Downloader

根据请求下载网页

#### Scheduler

调度管理

#### Middleware

修改丢弃请求和响应

用户编写

#### Spider

- 解析Downloader返回的响应
- 产生爬取项
- 产生额外的爬取请求

用户编写

#### Item Pipeline

- 流水线方式处理Spider的Item
- 一组操作顺序pipeline
- 清理，检验，查重HTML数据，并存储

#### Spider Middleware

- 对请求和爬取项再处理

- 修改，丢弃，新增请求或爬取项

### 和request的比较

scrapy是网站级爬虫，并发性好，深度定制困难

- 小需求，requests
- 中等需求，scrapy
- 定制高，自搭框架

### 常用命令

startproject

genspider

settings

crawl

list

shell

#### start 文档结构

![1550490771418](C:\Users\surface\AppData\Roaming\Typora\typora-user-images\1550490771418.png)

1. 建立爬虫项目
2. 产生一个scrapy爬虫

parse 用于处理响应，解析内容形成字典，发现新的url爬取请求

3. 配置产生的爬虫
   1. 初始url
   2. 获取页面后的解析方法
4. 编写Item Pipeline
5. 优化配置策略

Request类：http请求, Spider生成Downloader执行

 - url
 - method
 - headers
 - body
 - meta
 - copy()

Response类：HTTP响应，Downloader生成，Spider处理

Item类：HTML页面的信息内容，SPider生成，Item Pipeline处理

## 股票实例讲解

1. 首先建立项目和spider模板
2. 编写spider

从start开始发出request，指向parse，一番处理，然后重新发出Request，callback指向下一个parse，一番处理, 获得Item。

1. 编写Pipeline处理数据

修改setting，然后让pipeline自动处理，spider传过来的数据

