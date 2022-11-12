import json
res = {}
with open('all_tags_taken.txt','r',encoding ='utf-8') as f:
    lines = f.readlines()
tags = [x.split('\n')[0].upper() for x in lines]
for tag in tags:
    res[tag] = 0
for i in range(1,21):
    with open('data/cnblogs_data/experiment_data/articles_'+str(i)+'_after.json','r',encoding = 'utf-8') as f:
        articles = json.load(f)

    for article in articles:
        txt = ''.join(article['texts']).upper()
        title = article['title'].upper()
        for tag in tags:
            if title.find(tag)!=-1:
                res[tag]+=1
    print(i)
for r in res:
    print(r+' '+str(res[r]))