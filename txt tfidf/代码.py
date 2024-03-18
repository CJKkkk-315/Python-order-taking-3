import jieba
from collections import defaultdict
import os
import matplotlib.pyplot as plt
import pandas as pd
import math
from collections import Counter
plt.rcParams['font.sans-serif'] = ['SimHei']
# 文档分类分词预处理
def fenci():
    texts = defaultdict(list)
    with open('stopwords.txt', 'r', encoding='UTF-8') as meaninglessFile:
        stopwords = set(meaninglessFile.read().split('\n'))
    stopwords.add(' ')
    with open('cnews.test.txt','r',encoding='UTF8') as f:
        for i in f.readlines():
            cate,*text = i.replace('\n','').split()
            content = ''.join(text)
            content = list(jieba.cut(content))
            words = []
            for word in content:
                if word not in stopwords:
                    words.append(word)
            texts[cate].append(' '.join(words))
    n = 0
    for key in texts:
        with open(f'预处理结果\\{key}.txt','w',encoding='UTF8') as f:
            for item in texts[key]:
                f.write(str(n) + ' ' + item+'\n')
                n += 1
# 文章数量，平均词频可视化
def analysis():
    d = {}
    fileList = os.listdir('预处理结果')
    for file in fileList:
        with open(f'预处理结果\\{file}','r',encoding='UTF8') as f:
            d[file] = list(f.readlines())
    xy = list(d.items())
    x = [i[0].replace('.txt','') for i in xy]
    y = [len(i[1]) for i in xy]
    plt.bar(x,y)
    plt.title('不同分类的文章数量')
    plt.show()
    x = [i[0].replace('.txt', '') for i in xy]
    y = [sum([len(j.split()) for j in i[1]])//1000 for i in xy]
    plt.bar(x, y)
    plt.title('不同分类的平均词数量')
    plt.show()
def keyword():
    fileList = os.listdir('预处理结果')
    for file in fileList:
        keywords = []
        with open(f'预处理结果\\{file}', 'r', encoding='UTF8') as f:
            for i in f.readlines():
                keywords.append(' '.join([k[0] for k in sorted(Counter(i.split()).items(),key=lambda x:x[1],reverse=True)][:3]))
        with open(f'关键词\\{file}','w',encoding='UTF8') as f:
            for i in keywords:
                print(i)
                f.write(i+'\n')

def tfidfzone():
    split_ress = []
    fileList = os.listdir('预处理结果')
    for file in fileList:
        with open(f'预处理结果\\{file}', 'r', encoding='UTF8') as f:
            for i in f.readlines():
                aw = []
                for j in i.split():
                    aw.append(j)
                split_ress.append(aw)
    split_ress = split_ress[::100]
    print(len(split_ress))
    # 1.声明文档 分词 去重合并
    wordSet = set(split_ress[0])
    for i in split_ress[1:]:
        wordSet = wordSet.union(i)
    # 2.统计词项tj在文档Di中出现的次数，也就是词频。
    def computeTF(wordSet, split):
        tf = dict.fromkeys(wordSet, 0)
        for word in split:
            tf[word] += 1
        return tf
    tfs = []
    for i in split_ress:
        tfs.append(computeTF(wordSet, i))
    # 3.计算逆文档频率IDF
    def computeIDF(tfList):
        idfDict = dict.fromkeys(tfList[0], 0)  # 词为key，初始值为0
        N = len(tfList)  # 总文档数量
        for tf in tfList:  # 遍历字典中每一篇文章
            for word, count in tf.items():  # 遍历当前文章的每一个词
                if count > 0:  # 当前遍历的词语在当前遍历到的文章中出现
                    idfDict[word] += 1  # 包含词项tj的文档的篇数df+1
        for word, Ni in idfDict.items():  # 利用公式将df替换为逆文档频率idf
            idfDict[word] = math.log10(N / Ni)  # N,Ni均不会为0
        return idfDict  # 返回逆文档频率IDF字典
    idfs = computeIDF(tfs)
    # 4.计算tf-idf(term frequency–inverse document frequency)
    def computeTFIDF(tf, idfs):  # tf词频,idf逆文档频率
        tfidf = {}
        for word, tfval in tf.items():
            tfidf[word] = tfval * idfs[word]
        return tfidf
    tfidfs = []
    for i in tfs:
        tfidfs.append(computeTFIDF(i, idfs))
    tfidf = pd.DataFrame(tfidfs)
    print(tfidf)
    aw = dict.fromkeys(wordSet, 0)
    q = input('请输入关键词：')
    split_q = q.split()  # 分词
    nsq = []
    for i in split_q:
        if i in aw:
            nsq.append(i)
    split_q = nsq[::]
    tf_q = computeTF(wordSet, split_q)  # 计算Q的词频
    tfidf_q = computeTFIDF(tf_q, idfs)  # 计算Q的tf_idf(构建向量)
    ans = pd.DataFrame(tfidfs + [tfidf_q])
    # print(ans)
    res = []
    # 6.计算Q和文档Di的相似度（可以简单地定义为两个向量的内积）
    b = sum(list(map(lambda x: x ** 2, list(ans.loc[len(split_ress), :])))) ** 0.5
    for i in range(len(split_ress)):
        nj = (ans.loc[i, :] * ans.loc[len(split_ress), :]).sum()
        a = sum(list(map(lambda x: x ** 2, list(ans.loc[i, :])))) ** 0.5
        res.append([i, nj / (a * b)])
    res.sort(key=lambda x: x[1], reverse=True)
    f = []
    for i in res:
        if i[1] and not pd.isna(i[1]):
            f.append(i)
    res = f[::]
    with open('cnews.test.txt','r',encoding='UTF8') as f:
        pdata = f.readlines()
    for i in res:
        content = pdata[int(split_ress[i[0]][0])]
        beautiful_content = ''
        for n in range(len(content)):
            beautiful_content += content[n]
            if n%80 == 0 and n != 0:
                beautiful_content += '\n'
        print(f'相似度{i[1]},相似文章：')
        print(beautiful_content)
tfidfzone()