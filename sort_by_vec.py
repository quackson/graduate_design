import json
import numpy as np
with open('w2v.json','r',encoding='utf-8') as f:
    vec = json.load(f)
with open('all_tags_taken.txt','r',encoding ='utf-8') as f:
    lines = f.readlines()
tags = [x.split('\n')[0] for x in lines]
res = {}
for i,tag1 in enumerate(tags):
    res[tag1] = []
    temp = {}
    for tag2 in tags:
        a1 = np.array(vec[tag1])
        a2 = np.array(vec[tag2])
        norm1 = np.linalg.norm(a1)
        norm2 = np.linalg.norm(a2)
        r = 1/2*(1+np.dot(a1,a2)/(norm1*norm2))
        temp[tag2] = r
    temp = sorted(temp.items(), key=lambda x: x[1], reverse=True)
    for _ ,j in enumerate(temp):
        if _ > 3:
            break
        res[tag1].append(j[0])
    if i%100==0:
        print(i,'over')
with open('related_words.json','w',encoding ='utf-8') as f:
    json.dump(res,f,ensure_ascii=False)