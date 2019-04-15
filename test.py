# -*- coding: utf-8 -*-

import jsonpath
import json


row = {'id': 10378717, 'com_id': 32702950, 'year': 2019, 'month': 4, 'day': 12, 'name': '青铜建服', 'logo': 'https://cdn.itjuzi.com/images/d5ad7dc797cdc1c741b9d4ca7839e5db.png?imageView2/0/q/100', 'com_scope': '硬件', 'com_sub_scope': '综合硬件', 'round': '天使轮', 'money': '数千万人民币', 'money_num': 3000, 'investor': [{'type_id': 2, 'name': '丰厚资本（领投）', 'id': 205, 'url': 'https://www.itjuzi.com/investfirm/205', 'type': '领投'}, {'type_id': 7, 'name': '麒麟创投', 'url': '', 'type': '非结构化跟投'}], 'valuation': 15000, 'prov': '江苏', 'city': '南京', 'well_known_enterprises': False, 'well_known_fa': False, 'well_known_wind_cast': True, 'one_year': False, 'two_year': False, 'nicorn': False, 'maxima': False, 'time': 1554998400, 'agg_time': '2019-04-12', 'location': 'in', 'slogan': '建筑安全领域的人工智能科技品牌', 'com_registered_name': '南京榭客智能科技有限公司', 'com_des': '南京青铜建服科技有限公司，致力于在DT时代，运用物联网、大数据、生物识别等新科技，以数据为基础，不断创新安全管理、培训和监测诊断技术；以实现施工安全“零事故”为使命，构建全国200万建筑安全人的领先平台。\r\n\r\n公司核心团队来自中建、BAT、政府及行业精英，拥有独立的研发团队，拥有行业专家团队10人，建筑安全相关著作和专利15项，并获得江苏省行业5项奖励，全国创业创新奖励2项。\r\n\r\n公司坚持用户至上，自主研发智能安全产品，包含：安全大数据智能管理系统、安全诊断评价系统、安全培训系统、新一代智慧工地物联平台等解决方案，致力于成为最具品牌价值的建筑科技服务平台。', 'invse_title': '青铜建服获得数千万人民币天使轮融资，丰厚资本领投，麒麟创投参投', 'invse_des': '青铜建服是一个聚焦施工安全领域的人工智能安全大数据服务平台，近日，青铜建服正式对外发布，完成了数千万元人民币的天使轮融资，本轮融资由丰厚资本领投，麒麟创投等跟投。', 'com_tag': [{'tag_id': 247, 'tag_name': '人工智能'}, {'tag_id': 508, 'tag_name': '建筑行业'}, {'tag_id': 710, 'tag_name': '硬件'}, {'tag_id': 720, 'tag_name': '综合硬件'}], 'term_tag': [{'tag_id': 247, 'tag_name': '人工智能'}, {'tag_id': 508, 'tag_name': '建筑行业'}, {'tag_id': 710, 'tag_name': '硬件'}, {'tag_id': 720, 'tag_name': '综合硬件'}], 'currency': '人民币', 'spider_time': '2019-04-13 23:13:49'}
list_key = ['spider_time', 'agg_time', 'name', 'com_scope', 'investor_name', 'investor_type', 'prov',  'city', 'round', 'money', 'com_des']
spider_time = jsonpath.jsonpath(row, '$.spider_time')
agg_time = jsonpath.jsonpath(row, '$.agg_time')
name = jsonpath.jsonpath(row, '$.name')
com_scope = jsonpath.jsonpath(row, '$.com_scope')
investor_name = jsonpath.jsonpath(row, '$..investor..name[0,1]')
investor_type = jsonpath.jsonpath(row, '$..investor..type[0,2]')
prov = jsonpath.jsonpath(row, '$.prov')
city = jsonpath.jsonpath(row, '$.city')
round = jsonpath.jsonpath(row, '$.round')
money = jsonpath.jsonpath(row, '$.money')
com_des = jsonpath.jsonpath(row, '$..com_des')
list_value = spider_time + agg_time + name + com_scope + investor_name + investor_type + prov + city  + round + money + com_des
row = dict(zip(list_key, list_value))
print(row)
