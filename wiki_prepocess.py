import json
import requests
import re
import urllib
import time
from bs4 import BeautifulSoup as bs
res = dict()
tags = []
with open('DSA_data/all_tags_taken.txt','r',encoding = 'utf-8') as f:
    lines = f.readlines()
tags += [x.split('\n')[0] for x in lines]
with open('MLDL_data/all_tags_taken.txt','r',encoding = 'utf-8') as f:
    lines = f.readlines()
tags += [x.split('\n')[0] for x in lines]
with open('Java_data/all_tags_taken.txt','r',encoding = 'utf-8') as f:
    lines = f.readlines()
tags += [x.split('\n')[0] for x in lines]
tags = list(set(tags))
for i,tag in enumerate(tags):
    print(tag)
    key = tag
    if tag=='协同过滤':
        tag = '協同過濾'
    elif tag == '推荐系统':
        tag = '推薦系統'
    elif tag == '关键字':
        tag='保留字'
    elif tag =='正则化':
        tag = '正則化'
    elif tag=='复杂度':
        tag='計算複雜性理論'
    elif tag=='后序':
        tag='后记'
    elif tag=='解码':
        tag='编码'
    elif tag=='构造方法':
        tag='构造器'
    elif tag=='抽象数据类型':
        tag='抽象資料型別'
    elif tag=='自动驾驶':
        tag='自動駕駛'
    elif tag=='基本类型':
        tag='原始型別'
    elif tag=='数据类型':
        tag='資料類型'
    elif tag=='重载':
        tag='运算符重载'
    
    elif tag=='虚方法':
        tag='虚函数'
    #time.sleep(3)
    url = 'https://mwiki.footing.dev/w/index.php?title=Special:链入页面/'+tag+'&limit=5000'
    #url = 'https://zh.wikipedia.org/w/index.php?title=Special:链入页面/'+tag+'&limit=5000'
    attempts = 0
    success = False
    while attempts < 100 and not success:
        try:
            rp = requests.get(url)
            success = True
        except:
            attempts += 1
            if attempts == 10:
                print('get wiki fucked up',url)
                break
    if not success:
        continue
    if rp.status_code!=200:
        print(url,'status code failed',rp.status_code)
        continue
    soup = bs(rp.text,'lxml')
    ul = soup.find('ul',id='mw-whatlinkshere-list')
    inlinks = []
    raw_inlinks = ul.findAll('a')
    for raw_inlink in raw_inlinks:
        inlinks.append(raw_inlink.text)
    inlinks = inlinks[::3]
    final_links = []
    for inlink in inlinks:
        if ':' not in inlink:
            final_links.append(inlink)
    res[key] = final_links
with open('inlinks.json','w',encoding='utf-8') as f:
    json.dump(res,f)