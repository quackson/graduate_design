from sklearn.cluster import KMeans
import json
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
with open('all_tags_taken.txt','r',encoding ='utf-8') as f:
    lines = f.readlines()
tags = [x.split('\n')[0] for x in lines]
with open('feature_res.json','r',encoding ='utf-8') as f:
    data = json.load(f)
with open('positive_labels.txt','r',encoding ='utf-8') as f:
    lines = f.readlines()
positive_labels = [x.split('\n')[0] for x in lines]
with open('negative_labels.txt','r',encoding ='utf-8') as f:
    lines = f.readlines()
negative_labels = [x.split('\n')[0] for x in lines]
'''
new_positive_labels = []
for p_label in positive_labels:
    segs = p_label.split('#')
    if segs[0] in tags and segs[1] in tags:
        new_positive_labels.append(p_label)
new_negative_labels = []
for n_label in negative_labels:
    segs = n_label.split('#')
    if segs[0] in tags and segs[1] in tags:
        new_negative_labels.append(n_label)
with open('new_positive_labels.txt','w',encoding ='utf-8') as f:
    for p in new_positive_labels:
        f.write(p+'\n')
with open('new_negative_labels.txt','w',encoding ='utf-8') as f:
    for n in new_negative_labels:
        f.write(n+'\n')
exit()
'''

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
negative_x1 = list(set(negative_x1))[:500]
negative_x2 = list(set(negative_x2))[:500]

positive_x1_data = [data[x] for x in positive_x1]
positive_x2_data = [data[x] for x in positive_x2]
negative_x1_data = [data[x] for x in negative_x1]
negative_x2_data = [data[x] for x in negative_x2]
x = positive_x1_data+positive_x2_data+negative_x1_data+negative_x2_data
y = [1]*len(positive_x1)+[2]*len(positive_x2)+[0]*(len(negative_x1)*2)

from imblearn.over_sampling import SMOTE, ADASYN
x, y = ADASYN().fit_resample(x, y)

'''
raw_keys = []
for d in data:
    #if d not in positive_x1 and d not in negative_x1 and d not in positive_x2 and d not in negative_x2:
    raw_keys.append(d)
x_test = []
for raw_key in raw_keys:
    x_test.append(data[raw_key])
#clf = RandomForestClassifier(n_estimators=10,max_features=7, max_depth=None,min_samples_split=2, bootstrap=True)
clf = ExtraTreesClassifier(n_estimators=10,max_features=7, max_depth=None,min_samples_split=2, bootstrap=False)
clf.fit(x,y)
y_predict = clf.predict(x_test)
y_predict_prob = clf.predict_proba(x_test)
num0 = 0
num1 = 0
num2 = 0
for _ in y_predict:
    if _== 0:
        num0+=1
    if _ == 1:
        num1+=1
    if _ == 2:
        num2+=1
print(len(y_predict))
print(num0)
print(num1)
print(num2)

res = list(zip(raw_keys,y_predict))
res_prob = list(zip(raw_keys,y_predict_prob))
#print(res_prob)
print(len(res))
res_dict = {}
for i,r in enumerate(res):
    res_dict[r[0]] = (int(r[1]),float(max(res_prob[i][1])))
with open('res_dict_test.json','w',encoding = 'utf-8') as f:
    json.dump(res_dict,f,ensure_ascii=False)
'''
'''
with open('label_res.txt','w',encoding='utf-8') as f:
    
    
    for r in res:
        if r[1]==0:
            f.write(r[0]+' No relationship\n')
    for r in res:
        if r[1]==1:
            f.write(r[0]+' a->b\n')
    for r in res:
        if r[1]==2:
            f.write(r[0]+' b->a\n')
    '''


p1 = 0
p2 = 0
p3 = 0
p4 = 0 
f1 = 0
f2 = 0
f3 = 0
f4 = 0
r1 = 0
r2 = 0
r3 = 0
r4 = 0
for j in range(10):
    x_train, x_test, y_train, y_test = train_test_split(x, y, random_state=j+1, train_size=0.7)
    clf1 = DecisionTreeClassifier(max_depth=None, min_samples_split=2,random_state=0)
    clf2 = RandomForestClassifier(n_estimators=10,max_features=7, max_depth=None,min_samples_split=2, bootstrap=True)
    clf3 = ExtraTreesClassifier(n_estimators=10,max_features=7, max_depth=None,min_samples_split=2, bootstrap=False)
    clf_xgb = XGBClassifier(
        n_estimators=30,#三十棵树
        learning_rate =0.3,
        max_depth=3,
        min_child_weight=1,
        gamma=0.3,
        subsample=0.8,
        colsample_bytree=0.8,
        objective= 'macro:logistic',
        nthread=12,
        scale_pos_weight=1,
        reg_lambda=1,
        seed=27)

    clf1.fit(x_train, y_train)
    clf2.fit(x_train, y_train)
    clf3.fit(x_train, y_train)
    clf_xgb.fit(np.array(x_train), np.array(y_train))
    y_predict1 = clf1.predict(x_test)
    y_predict2 = clf2.predict(x_test)
    y_predict3 = clf3.predict(x_test)
    y_predict4 = clf_xgb.predict(np.array(x_test))
    f1 += sklearn.metrics.f1_score(y_test, y_predict1,average='macro')
    f2 += sklearn.metrics.f1_score(y_test, y_predict2,average='macro')
    f3 += sklearn.metrics.f1_score(y_test, y_predict3,average='macro')
    f4 += sklearn.metrics.f1_score(y_test, y_predict4,average='macro')
    r1 += sklearn.metrics.recall_score(y_test, y_predict1, average='macro')
    r2 += sklearn.metrics.recall_score(y_test, y_predict2, average='macro')
    r3 += sklearn.metrics.recall_score(y_test, y_predict3, average='macro')
    r4 += sklearn.metrics.recall_score(y_test, y_predict4, average='macro')
    for i,yy in enumerate(y_test):
        if y_predict1[i]==yy:
            p1+=1
        if y_predict2[i]==yy:
            p2+=1
        if y_predict3[i]==yy:
            p3+=1
        if y_predict4[i]==yy:
            p4+=1
l =  len(y_test)*10
print('p1',p1/l)
print('p2',p2/l)
print('p3',p3/l)
print('p4',p4/l)
print('f1',f1/10)
print('f2',f2/10)
print('f3',f3/10)
print('f4',f4/10)
print('r1',r1/10)
print('r2',r2/10)
print('r3',r3/10)
print('r4',r4/10)

'''
features = list(data.values())
x = np.array(features)
x_normed = x / x.max(axis=0).tolist()
data = zip(list(data.keys()),x_normed)
res = sorted(data, key=lambda item:sum(item[1]), reverse=True)
with open('positive_label.txt','r',encoding ='utf-8') as f:
    lines = f.readlines()
positive_labels = [x.split('\n')[0] for x in lines]
print(positive_labels[0])
with open('labeling.txt','w',encoding = 'utf-8') as f:
    for r in res[:5000]:
        if r[0] not in positive_labels:
            f.write(r[0]+'\n')
exit()
label = KMeans(n_clusters=2, random_state=9).fit_predict(x_normed.tolist())
#res = {}
with open('label_res.txt','w',encoding = 'utf-8') as f: 
    for i,key in enumerate(data):
        f.write(str(key)+' '+str(label[i])+'\n')

with open('label_res.json','w',encoding ='utf-8') as f:
    json.dump(res,f,ensure_ascii=False)
'''