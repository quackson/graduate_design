import json
import hanlp
from pyhanlp import *
import numpy as np
'''
HanLP = hanlp.load(hanlp.pretrained.mtl.UD_ONTONOTES_TOK_POS_LEM_FEA_NER_SRL_DEP_SDP_CON_XLMR_BASE)
print(HanLP(['C++','网络安全']))'''
#todo
with open('all_tags_taken.txt','r',encoding ='utf-8') as f:
    lines = f.readlines()
tags = [x.split('\n')[0] for x in lines]

pre = {}
res = {}
err = []
with open('sgns.wiki.bigram-char','r',encoding = 'utf-8') as f:
    line = f.readline()
    line = f.readline()
    while line:
        word = line.split(' ')[0]
        vec = line.split(' ')[1:-1]
        pre[word.upper()] = [float(x) for x in vec]
        line = f.readline()
t = np.sum([pre['友'],pre['元']], axis = 0)
pre['友元'] = [x/2 for x in t]
t = np.sum([pre['向'],pre['量']], axis = 0)
pre['向量'] = [x/2 for x in t]
t = np.sum([pre['引'],pre['擎']], axis = 0)
pre['引擎'] = [x/2 for x in t]
t = np.sum([pre['搜索'],pre['引擎']], axis = 0)
pre['搜索引擎'] = [x/2 for x in t]
t = np.sum([pre['缺'],pre['页']], axis = 0)
pre['缺页'] = [x/2 for x in t]
t = np.sum([pre['中断'],pre['向量']], axis = 0)
pre['中断向量'] = [x/2 for x in t]
t = np.sum([pre['K'],pre['MEANS']], axis = 0)
pre['K-MEANS'] = [x/2 for x in t]
t = np.sum([pre['I'],pre['PYTHON']], axis = 0)
pre['IPYTHON'] = [x/2 for x in t]
print('over')
for i,tag in enumerate(tags):
    raw_segs = HanLP.segment(tag)
    segs = []
    for raw_seg in raw_segs:
        if str(raw_seg)[0]==' ':
            continue
        elif str(raw_seg)[0]!='/':
            segs.append(str(raw_seg).split('/')[0])
        elif str(raw_seg)[1]=='/':
            segs.append('/')
    try:
        temp = []
        for seg in segs:
            temp.append(pre[seg.upper()])
        r = np.sum(temp, axis = 0)
        l = len(segs)
        r = [x/l for x in r]
        res[tag] = r
    except:
        err.append(tag)
    if i%100==0:
        print(i,'over')

with open('word_unconverted.txt','w',encoding ='utf-8') as f:
    for e in err:
        f.write(e+'\n')
with open('w2v.json','w',encoding ='utf-8') as f:
    json.dump(res,f,ensure_ascii=False)