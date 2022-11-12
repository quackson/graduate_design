import os
import json
#course_list = ['convolutional-neural-networks','deep-neural-network','machine-learning','machine-learning-projects','ml-clustering-and-retrieval','ml-foundations','neural-networks-deep-learning','nlp-sequence-models']
#course_list = ['data-structures-algorithms-1','data-structures-algorithms-2','data-structures-algorithms-3','data-structures-algorithms-4','gaoji-shuju-jiegou','shuju-jiegou-suanfa','suanfa-jichu']
course_list = ['java-chengxu-sheji','java-programming','java-programming-arrays-lists-data','java-programming-design-principles','java-programming-recommender','object-oriented-java']
root_dir = 'data/mooc_data/coursera/'
def crawl(course_name):
    course_dir = root_dir+course_name
    res = {}
    res['name'] = course_name
    res['captions'] = []
    sections = os.listdir(course_dir)
    num = 0
    for section in sections:
        section_dir = course_dir+'/'+section
        subsections = os.listdir(section_dir)
        for subsection in subsections:
            subsection_dir = section_dir+'/'+subsection
            txts = os.listdir(subsection_dir)
            for txt in txts:
                content = {}
                num+=1
                content['id'] = num
                '''
                content['section']=  section.split('_')[0].lstrip('0')
                content['subsection'] = subsection.split('_')[0].lstrip('0')
                content['chapter'] = txt.split('_')[0].lstrip('0')
                '''
                with open(subsection_dir+'/'+txt,'r',encoding = 'utf-8') as f:
                    text = '。'.join(f.readlines())
                    text = text.replace('\n ','。')
                    l = len(text)
                    r = ''
                    d = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ+-0123456789'
                    for i in range(1,l):
                        if text[i]==' ' and text[i-1] not in d and text[i+1] in d:
                            continue
                        if text[i]==' ' and text[i+1] not in d and text[i-1] in d:
                            continue
                        r+=text[i]
                    r = r.upper()
                    #text = text.replace(' ','')
                    content['text'] = r
                res['captions'].append(content)
    return res

if __name__ == '__main__':
    for course_name in course_list:
        course_content = crawl(course_name)
        
        with open('data/mooc_data/coursera_data/'+course_name+'.json','w',encoding = 'utf-8') as f:
            json.dump(course_content,f,ensure_ascii = False)
        
