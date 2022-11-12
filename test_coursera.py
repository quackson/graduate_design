#course_list = ['convolutional-neural-networks','deep-neural-network','machine-learning','machine-learning-projects','ml-clustering-and-retrieval','ml-foundations','neural-networks-deep-learning','nlp-sequence-models']
#course_list = ['data-structures-algorithms-1','data-structures-algorithms-2','data-structures-algorithms-3','data-structures-algorithms-4','gaoji-shuju-jiegou','shuju-jiegou-suanfa','suanfa-jichu']
course_list = ['java-chengxu-sheji','java-programming','java-programming-arrays-lists-data','java-programming-design-principles','java-programming-recommender','object-oriented-java']

import json
with open('data/tags_data/all_tags_after.txt','r',encoding ='utf-8') as f:
    lines = f.readlines()
tags = [x.split('\n')[0] for x in lines]
text = ''
for course_name in course_list:
    with open('data/mooc_data/coursera_data/'+course_name+'.json','r',encoding = 'utf-8') as f:
        course_content = json.load(f)
    
    for caption in course_content['captions']:
        text+=caption['text']

tag_num=0
res=[]
for tag in tags:
    num = text.count(tag.upper())
    if num>19:
        res.append(tag)
print(len(res))
with open('all_tags_taken.txt','w',encoding ='utf-8') as f:
    for e in res:
        f.write(e+'\n')
