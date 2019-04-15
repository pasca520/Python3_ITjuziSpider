# ITjuziSpider


## 1、思路
这个脚本是用来爬取it桔子的免费投融资信息的，利用cookie信息，模拟登陆，然后导入到mongoDB里面。
对于我来说，主要遇到了两个难点。
- 1、如何处理模拟登陆的环节
- 2、导入数据如何保证mongoDB中数据不重复

关于第一点，主要是根据https://curl.trillworks.com/这个网站复制的curl请求。
然后直接查看cookie信息的构造，最后利用利用账号密码生成token信息请求

关于第二点，试踩了很多坑，最后发现，不用insert_one直接插入，而是用update_one更新更好一点，mycol.update_one(row, {'$setOnInsert': row}, upsert=True)


## 2、依赖库

import requests
import random
import string
from configparser import ConfigParser
import json
import jsonpath
import time
import pymongo
import csv

其中，如果jsonpath和csv没有实际使用到，jsonpath是一个json解析库，可以自定义json的资源。csv是我想直接导入到csv文件，后来想想，还是没弄了。
后续有时间再整整。


## 3、注意点
1、只能爬取三页，而且没做啥防爬措施
2、业务学习使用# Python3_ITjuziSpider
# Python3_ITjuziSpider
