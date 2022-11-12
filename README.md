# Fragmented Learning System based on MOOC

## data

所有爬到的慕课平台/博客园平台/维基百科/标签的数据
+ cnblogs_data: 博客园的数据和爬虫代码
+ mooc_data: coursera/imooc/学堂在线的数据和爬虫代码
+ tags_data: 所有标签和相关代码
+ wiki_data: 维基百科数据和爬虫代码

## metadata

经过算法生成的各个关键词之间的关系数据

## system

前后端代码，后端用flask，前端用Vue.js
+ backend.py: 后端
+ 其他: 前端

## 其他代码

+ classifier.py: 利用关系抽取后得到的关系向量对关键词之间的关系进行分类
+ course2tag.py: 将课程绑定到tag
+ coursera_preprocess.py: 对爬取到的coursera字幕数据进行预处理
+ draw.py: 对得到的关系图利用pyecharts进行可视化
+ featuregenerator.py: 利用公式进行关系向量抽取
+ frontend.py: 将边数据进行处理，便于前端使用
+ label_filter.py: 对标签进行筛选，选取出现频率较高的
+ RefD.py: 对分类结果进行统计
+ sort_by_vec.py: 利用向量间相似度进行排序
+ wiki_preprocess.py: 对爬取到的wiki百科数据进行预处理
+ word2vec.py: 将word转化为词向量