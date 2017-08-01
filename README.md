# gambling_sites_judgment
使用贝叶斯算法判断一个网站是否为博彩网站

训练样本分为两类，一类是各种新闻页面，另一类则是博彩页面

博彩页面来源：
1、百度根据关键词搜索，然后过滤
2、360搜索根据关键词搜索，然后过滤
3、其他途径获取每天新解析的DNS对应的域名数据，然后过滤


目录结构：
|
|----bayes_training_outcome  #贝叶斯训练结果
|
|----data  
|      |----data          #保存提取后的关键页面内容；
|      |----original_data #保存页面原始内容；
|      |----test          #贝叶斯测试数据，
|      |----training      #贝叶斯训练数据
|
|----medfiles #保存各类样本中出现的单词及其出现次数
|
|----outcome #测试结果
| 
|--bayesclassifier.py #贝叶斯测试脚本
|
|--bayestraining.py #贝叶斯训练脚本
|
|--fre.py #词频统计等
|
|--parseurl.py #解析页面获取数据，在bayesclassifier.py会调用
|
|--judge_bocai.py #采集训练数据的时候会用到，判断某一个url是否为博彩网站
|
|--get_page_content.py #获取网站的页面数据