import json
import numpy as np
import random
'''
with open('all_tags_taken.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
tags = [x.split('\n')[0] for x in lines]
with open('old_metadata/positive_label.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
labels = [x.split('\n')[0] for x in lines]
positive_labels = []
for label in labels:
    segs = label.split('#')
    if segs[0] in tags and segs[1] in tags:
        positive_labels.append(label)
with open('old_metadata/negative_label.txt','r',encoding='utf-8') as f:
    lines = f.readlines()
labels = [x.split('\n')[0] for x in lines]
negative_labels = []
for label in labels:
    segs = label.split('#')
    if segs[0] in tags and segs[1] in tags:
        negative_labels.append(label)
print(len(positive_labels))
print(len(negative_labels))
with open('positive_labels.txt','w',encoding ='utf-8') as f:
    for e in positive_labels:
        f.write(e+'\n')
with open('negative_labels.txt','w',encoding ='utf-8') as f:
    for e in negative_labels:
        f.write(e+'\n')
'''
with open('feature_res.json','r',encoding='utf-8') as f:
    feature_data = json.load(f)
k = list(feature_data.keys())
random.shuffle(k)
with open('labelling.txt','w',encoding = 'utf-8') as f:
    for e in k[:2000]:
        f.write(e+'\n')