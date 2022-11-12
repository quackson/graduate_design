from flask import request, jsonify, Flask,  json, Response
import requests
import json
from flask_cors import *

app = Flask(__name__)
CORS(app, supports_credentials=True)
@app.route('/hello',methods=['GET'])
def index():
    return jsonify("Hello World")



'''
request:{
    'field':'MLDL'/'Java'/'DSA'
    'concept':concept-name
}
response:{
    'name':xxx,
    'outlinks':[{
        'name':xxx,
        'value':xxx
    }],
    'inlinks':[{
        'name':xxx,
        'value':xxx
    }],
}
'''
@app.route('/getRelatedConcept',methods = ['GET'])
def getRelatedCondept():
    field = request.args.get('field')
    concept = request.args.get('concept')
    trans = {
        '数据结构与算法':'DSA',
        '机器学习':'MLDL',
        'Java编程':'Java'
    }
    field = trans[field]
    with open(field+'_edges.json','r',encoding='utf-8') as f:
        data = json.load(f)
    res = {
        'name':concept,
        'outlinks':[{'name':x['name'],'value':x['value']/2} for x in data[concept]['outlinks']],
        'inlinks':[{'name':x['name'],'value':x['value']/2} for x in data[concept]['inlinks']]
    }
    return jsonify(res)

'''
request:{
    'concept':name
    'startNum':num
}
response:{
    articles:[
        {
            'title':xxx,
            'id':x,
            'url':url
            'summary':short text
        }
    ]
}
'''
@app.route('/getArticleList',methods = ['GET'])
def getArticleList():
    concept = request.args.get('concept')
    startNum = int(request.args.get('startNum'))
    with open('concept&articles.json','r',encoding='utf-8') as f:
        data = json.load(f)
    articleList = data[concept][startNum:startNum+10]
    res = {
        'articles':[]
    }
    for article in articleList:
        res['articles'].append({
            'title':article['title'],
            'id':article['id'],
            'url':article['url'],
            'summary':article['summary']
        })
    return jsonify(res)


'''
request:{
    'concept':name
    'articleID':id
}
response:{
    'title':xxx
    'id':id
    'text': text
    'url':url
}
'''
@app.route('/getArticle',methods = ['GET'])
def getArticle():
    concept = request.args.get('concept')
    articleID = request.args.get('articleID')
    with open('concept&articles.json','r',encoding='utf-8') as f:
        data = json.load(f)
    article = data[concept][int(articleID)]
    res = {
        'title':article['title'],
        'id':article['id'],
        'url':article['url'],
        'text':article['text']
    }
    return jsonify(res)

if __name__ == '__main__':
    app.run(host ='127.0.0.1',port = 8000)