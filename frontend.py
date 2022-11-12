import json
fields = ['DSA','MLDL','Java']
concepts = []
for field in fields:
    res = {}
    with open(field+'_data/'+field+'_res_dict.json','r',encoding = 'utf-8') as f:
        edge_data = json.load(f)
    for k in edge_data:
        c1 = k.split('#')[0]
        c2 = k.split('#')[1]
        if c1 not in res.keys():
            res[c1] = {
                'outlinks':[],
                'inlinks':[]
            }
        if c2 not in res.keys():
            res[c2] = {
                'outlinks':[],
                'inlinks':[]
            }
        if edge_data[k][0]==1 and edge_data[c2+'#'+c1][0]==2:
            res[c2]['inlinks'].append({
                'name':c1,
                'value':(edge_data[k][1]+edge_data[c2+'#'+c1][0])/2
            })
            res[c1]['outlinks'].append({
                'name':c2,
                'value':(edge_data[k][1]+edge_data[c2+'#'+c1][0])/2
            })
    concepts+=list(res.keys())
    with open(field+'_edges.json','w',encoding='utf-8') as f:
        json.dump(res,f,ensure_ascii=False)
print('over')
concepts = list(set(concepts))
res = {}
for concept in concepts:
    res[concept]=[]
for i in range(1,21):
    with open('data/cnblogs_data/experiment_data/articles_'+str(i)+'_after.json','r',encoding = 'utf-8') as f:
        articles = json.load(f)

    for article in articles:
        txt = ''.join(article['texts']).upper()
        title = article['title'].upper()
        for concept in concepts:
            if len(res[concept])<100 and title.find(concept)!=-1:
                res[concept].append({
                    'title':article['title'],
                    'id':len(res[concept]),
                    'text':'xzh'.join(article['texts']),
                    'url':article['url'],
                    'summary':'。'.join(''.join(article['texts']).split('。')[:3])
                    })
    print(i)
with open('concept&articles.json','w',encoding='utf-8') as f:
    json.dump(res,f,ensure_ascii=False)