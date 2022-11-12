import json
import numpy as np
#course_list = ['convolutional-neural-networks','deep-neural-network','machine-learning','machine-learning-projects','ml-clustering-and-retrieval','ml-foundations','neural-networks-deep-learning','nlp-sequence-models']
#course_list = ['data-structures-algorithms-1','data-structures-algorithms-2','data-structures-algorithms-3','data-structures-algorithms-4','gaoji-shuju-jiegou','shuju-jiegou-suanfa','suanfa-jichu']
course_list = ['java-chengxu-sheji','java-programming','java-programming-arrays-lists-data','java-programming-design-principles','java-programming-recommender','object-oriented-java']

with open('related_words.json','r',encoding = 'utf-8') as f:
        related_words = json.load(f)
tag_pos = {}
with open('data/wiki_data/wiki_data.json','r',encoding = 'utf-8') as f:
    wiki_data = json.load(f)
def find_tag_pos(tag):
    tag_pos[tag] = {}
    for course in course_list:
        tag_pos[tag][course] = []
        with open('data/mooc_data/coursera_data/'+course+'.json','r',encoding = 'utf-8') as f:
            course_content = json.load(f)
            for caption in course_content['captions']:
                text=caption['text']
                if text.find(tag)!=-1:
                    tag_pos[tag][course].append(int(caption['id']))
                    
def word2vec(word):
    with open('w2v.json','r',encoding ='utf-8') as f:
        res = json.load(f)
        return res[word]
    
#todo 
def enrichWord(word):
    return []

#sementic relatedness
def SR(tag1,tag2):
    a1 = np.array(word2vec(tag1))
    a2 = np.array(word2vec(tag2))
    norm1 = np.linalg.norm(a1)
    norm2 = np.linalg.norm(a2)
    res = 1/2*(1+np.dot(a1,a2)/(norm1*norm2))
    return res

#video reference weight
def VRW(tag1,tag2):
    sum1 = 0
    sum2 = 0
    for course in course_list:
        if not tag_pos[tag1][course]:
            continue
        with open('data/mooc_data/coursera_data/'+course+'.json','r',encoding = 'utf-8') as f:
            course_content = json.load(f)
            for caption in course_content['captions']:
                text=caption['text']
                cnt = text.count(tag1)
                sum2+=cnt
                if text.find(tag2)!=-1:
                    sum1+=cnt
    if sum2==0:
        return 0
    res = sum1/sum2
    return res

def GVRW(tag1,tag2):
    ais = related_words[tag1]
    num1 = 0
    num2 = 0
    for ai in ais:
        t = SR(ai,tag2)
        num1+=(t*VRW(ai,tag2))
        num2+=t
    return num1/num2
    
#video reference distance
def GVRD(tag1,tag2):
    return GVRW(tag2,tag1)-GVRW(tag1,tag2)

#sentence reference weight
def SRW(tag1,tag2):
    sum1 = 0
    sum2 = 0
    for course in course_list:
        if not tag_pos[tag1][course]:
            continue
        with open('data/mooc_data/coursera_data/'+course+'.json','r',encoding = 'utf-8') as f:
            course_content = json.load(f)
            for caption in course_content['captions']:
                text=caption['text']
                sentences = text.split('，|。|！|？|；|“|”|、|‘|’')
                for sentence in sentences:
                    cnt = sentence.count(tag1)
                    sum2+=cnt
                    if sentence.find(tag2)!=-1:
                        sum1+=cnt
    if sum2==0:
        return 0
    res = sum1/sum2
    return res

def GSRW(tag1,tag2):
    ais = related_words[tag1]
    num1 = 0
    num2 = 0
    for ai in ais:
        t = SR(ai,tag2)
        num1+=(t*SRW(ai,tag2))
        num2+=t
    return num1/num2

#sentence reference distance
def GSRD(tag1,tag2):
    return GSRW(tag2,tag1)-GSRW(tag1,tag2)

#wikipedia reference eight
#todo 
def WRW(tag1,tag2):
    #if tag1 refer to tag2
    return 1
    
#wikipedia reference distance
def WRD(tag1,tag2):
    return WRW(tag1,tag2)-WRW(tag2,tag1)

#average position distance
def APD(tag1,tag2):
    num1 = 0
    num2 = 0
    for course in course_list:
        I1 = tag_pos[tag1][course]
        I2 = tag_pos[tag2][course]
        if len(I1)*len(I2)==0:
            continue
        num2+=1
        num1+=(np.mean(I2)-np.mean(I1))
    if num2==0:
        return 0
    return num1/num2

#distributional asymmetry distance
def DAD(tag1,tag2):
    
    num1 = 0
    num2 = 0
    for course in course_list:
        I1 = tag_pos[tag1][course]
        I2 = tag_pos[tag2][course]
        if len(I1)*len(I2)==0:
            continue
        num2+=1
        with open('data/mooc_data/coursera_data/'+course+'.json','r',encoding = 'utf-8') as f:
            course_content = json.load(f)
        SCres = 0
        SClen = 0
        for i in I1:
            for j in I2:
                if i>=j:
                    continue
                SClen+=1
                text1=course_content['captions'][i-1]['text']
                text2=course_content['captions'][j-1]['text']
                SCres+=(text1.count(tag1)-text2.count(tag2))
        if SClen!=0:
            num1+=(SCres/SClen)
    if num2==0:
        return 0
    return num1/num2

#average video coverage
def AVC(tag):
    num1=0
    num2=0
    for course in course_list:
        I = tag_pos[tag][course]
        if len(I)==0:
            continue
        with open('data/mooc_data/coursera_data/'+course+'.json','r',encoding = 'utf-8') as f:
            course_content = json.load(f)
        num2+=1
        num1+=(len(tag_pos[tag][course])/len(course_content['captions']))
    if num2==0:
        return 0
    return num1/num2

#average survival time
def AST(tag):
    num1=0
    num2=0
    for course in course_list:
        I = tag_pos[tag][course]
        if len(I)==0:
            continue
        with open('data/mooc_data/coursera_data/'+course+'.json','r',encoding = 'utf-8') as f:
            course_content = json.load(f)
        num2+=1
        num1+=((tag_pos[tag][course][-1]-tag_pos[tag][course][0]+1)/len(course_content['captions']))
    if num2==0:
        return 0
    return num1/num2

#complexity level distance
def CLD(tag1,tag2):
    return AVC(tag1)*AST(tag1)-AVC(tag2)*AST(tag2)

#wiki appearance
def WA(a,b):
    res = 0
    article = wiki_data[b]
    abstract = article['abstract']
    res+=abstract.count(a)
    return res

if __name__=="__main__":
    
    res = {}
    with open('all_tags_taken.txt','r',encoding ='utf-8') as f:
        lines = f.readlines()
    tags = [x.split('\n')[0] for x in lines]
    
    for tag in tags:
        find_tag_pos(tag)
    
    
    with open('tag_pos.json','w',encoding ='utf-8') as f:
        json.dump(tag_pos,f,ensure_ascii=False)
    
    for tag1 in tags:
        print(tag1)
        for tag2 in tags:
            if tag1==tag2:
                continue
            r = []
            r.append(SR(tag1,tag2))
            r.append(GVRD(tag1,tag2))#-
            r.append(GSRD(tag1,tag2))#-
            #r.append(GWRD(tag1,tag2))
            
            r.append(APD(tag1,tag2)) 
            r.append(DAD(tag1,tag2))
            r.append(CLD(tag1,tag2))
            r.append(WA(tag1,tag2))
            res[tag1+'#'+tag2] = r
    
    with open('feature_res.json','w',encoding ='utf-8') as f:
        json.dump(res,f,ensure_ascii=False)
    