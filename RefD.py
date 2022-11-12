import json
from opencc import OpenCC
from sklearn.cluster import KMeans
import numpy as np
import math
import warnings
from sklearn.model_selection import cross_val_score
from sklearn.datasets import make_blobs
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import ExtraTreesClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from xgboost.sklearn import XGBClassifier
import sklearn
'''
trans = OpenCC('t2s')  # 繁转简

with open('MLDL_data/all_tags_taken.txt','r',encoding = 'utf-8') as f:
    lines = f.readlines()
tags = [x.split('\n')[0] for x in lines]
outlinks = dict()
with open('inlinks.json','r',encoding = 'utf-8') as f:
    inlinks = json.load(f)
with open('data/wiki_data/wiki_data.json','r',encoding = 'utf-8') as f:
    wiki_data = json.load(f)
for tag in tags:
    outlinks[tag] = wiki_data[tag]['links']
for tag in tags:
    inlinks[tag] = [trans.convert(x) for x in inlinks[tag]]
    outlinks[tag] = [trans.convert(x) for x in outlinks[tag]]
def w(tag1,tag2):
    if tag1 in outlinks[tag2]:
        return 1
    return 0

def RD(tag1,tag2):
    sum1 = 0
    sum2 = 0
    for tag in tags:
        sum2+=w(tag,tag2)
        if tag1 in outlinks[tag]:
            sum1+=w(tag,tag2)
    if sum2==0:
        return 0
    return sum1/sum2
def RefD(tag1,tag2):
    return RD(tag1,tag2)-RD(tag2,tag1)
res = {}
for tag1 in tags:
    for tag2 in tags:
        if tag1==tag2:
            continue
        res[tag1+'#'+tag2] = RefD(tag1,tag2)
        
with open('MLDL_data/RefD.json','w',encoding='utf-8') as f:
    json.dump(res,f)
'''
with open('MLDL_data/positive_labels.txt','r',encoding ='utf-8') as f:
    lines = f.readlines()
positive_labels = [x.split('\n')[0] for x in lines]
with open('MLDL_data/negative_labels.txt','r',encoding ='utf-8') as f:
    lines = f.readlines()
negative_labels = [x.split('\n')[0] for x in lines]
positive_x1 = []
positive_x2 = []
for p_label in positive_labels:
    positive_x1.append(p_label)
for p_label in positive_labels:
    tags = p_label.split('#')
    pp_label = tags[1]+'#'+tags[0]
    positive_x2.append(pp_label)
negative_x1 = []
negative_x2 = []
for n_label in negative_labels:
    negative_x1.append(n_label)
for n_label in negative_labels:
    tags = n_label.split('#')
    nn_label = tags[1]+'#'+tags[0]
    negative_x2.append(nn_label)
positive_x1 = list(set(positive_x1))[:100]
positive_x2 = list(set(positive_x2))[:100]
negative_x1 = list(set(negative_x1))[:400]
negative_x2 = list(set(negative_x2))[:400]

x = positive_x1+positive_x2+negative_x1+negative_x2
y = [1]*len(positive_x1)+[2]*len(positive_x2)+[0]*(len(negative_x1)*2)
with open('MLDL_data/RefD.json','r',encoding='utf-8') as f:
    res = json.load(f)
y_predict = []
for i in x:
    if res[i]>0.1:
        y_predict.append(1)
    elif res[i]<-0.1:
        y_predict.append(2)
    else:
        y_predict.append(0)

f = sklearn.metrics.f1_score(y, y_predict,average='macro')
r = sklearn.metrics.recall_score(y, y_predict, average='macro')
s = 0
for i,j in enumerate(y):
    if j==y_predict[i]:
        s+=1
p = s/len(y)
#print(y_predict)
print(p)
print(r)
print(f)