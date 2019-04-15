# -*- coding: utf-8 -*-

import requests
import random
import string
from configparser import ConfigParser
import json
import jsonpath
import time
import pymongo
import csv

# 读取配置文件信息
cfg = ConfigParser()
cfg.read('config.ini')
userName = cfg.get('userInfo', 'userName')
passWord = cfg.get('userInfo', 'passWord')


# mongodb链接信息
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["ITjuzi"]
mycol = mydb["itjuziInvestevents"]

def Get_Token():
    url = "https://www.itjuzi.com/api/authorizations"
    Payload_Token = "{\"account\":\"%s\",\"password\":\"%s\"}" % (userName, passWord)  # \为转义字符
    cookie = ''.join(random.sample(string.ascii_letters + string.digits, 62))  # 随机生成62位字符串


# 构造请求token
    cookies = {
        'acw_tc': '%s'.format(cookie),
    }
    headers_token = {
        'Origin': 'https://www.itjuzi.com',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'CURLOPT_FOLLOWLOCATION': 'true',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
        'Content-Type': 'application/json;charset=UTF-8',
        'Accept': 'application/json, text/plain, */*',
        'Referer': 'https://www.itjuzi.com/login',
        'Connection': 'keep-alive',
    }

    res_token = requests.post(url, headers=headers_token, cookies=cookies, data= Payload_Token).text
    Json_token = json.loads(res_token)
    Token = Json_token['data']['token']
    return Token, cookie


# 根据token和cookie构造爬虫
def Crawl_one_page(Token, pageNumNow, cookie):
    headers = {
            'Origin': 'https://www.itjuzi.com',
            'Accept-Encoding': 'gzip, deflate, br',
            'Accept-Language': 'zh-CN,zh;q=0.9',
            'CURLOPT_FOLLOWLOCATION': 'true',
            'Authorization': '%s'%Token,
            'Content-Type': 'application/json;charset=UTF-8',
            'Accept': 'application/json, text/plain, */*',
            'Referer': 'https://www.itjuzi.com/investevent',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36',
            'Connection': 'keep-alive',
            'Cookie': '%s'%cookie
        }

    Payload_Investevents = '{"pagetotal":58797,"total":0,"per_page":20,"page":%s,"type":1,"scope":"","sub_scope":"","round":[],"valuation":[],"valuations":"","ipo_platform":"","equity_ratio":"","status":"","prov":"","city":[],"time":[],"selected":"","location":"\u56FD\u5185","currency":[],"keyword":""}'%pageNumNow
    response = requests.post('https://www.itjuzi.com/api/investevents', headers=headers, data=Payload_Investevents.encode('utf-8')).text
    data = json.loads(response)
    if data['status'] != 'success':
        print('遇到了反爬虫，休息10+秒')
        time.sleep(10 + random.random() * 5)
    rows = data['data']['data']
    return rows

# 插入MongoBD中
def Write_mongo(rows):
    for row in rows:
        # row['spider_time'] = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))   # 增加采集时间
        try:
            mycol.update_one(row, {'$setOnInsert': row}, upsert=True)   # 使用update_one，则已存在的不会在插入
        except:
            print('>>>>>>:', row, '已经存在')
            pass
if __name__ == '__main__':
    Token, cookie = Get_Token()
    for pageNumNow in range(1, 4):
        rows = Crawl_one_page(Token, pageNumNow, cookie)
        print('正在爬取第%s页写入MongoDB数据库' % pageNumNow)
        Write_mongo(rows)
    print('爬虫结束')
















