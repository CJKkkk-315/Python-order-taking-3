# import MySQLdb
import pymysql
import jieba
from snownlp import SnowNLP
import math
import pickle
import numpy as np
import pymysql
import pandas as pd
db = pymysql.connect("localhost",
                     "cjk123", "123456",
                     "接单",
                     charset='utf8')
cursor = db.cursor()
cursor.execute('select count(*) from `接单`.`doc_location`')
N = 1 + cursor.fetchall()[0][0]  # 文档总数
# print(N)
filenames = ['N01','N02','N03','N04','N05','N06','N07','N08','N09','N10','N11','N12','N13','N14','N15','N16']
aa = [10, 9, 17, 8, 10, 10, 15, 22, 23, 23, 12, 22, 25, 19, 23, 23]
for filename,a in zip(filenames,aa):
    target = ""
    if filename == 'N01':
        target = "请说说再生医学。"
    elif filename == 'N02':
        target = "美国对于贫铀炸弹的姿态"
    elif filename == 'N03':
        target = "“911”恐怖袭击后美国经济发生了什么变化？"
    elif filename == 'N04':
        target = "各国对洛克比空难的反应。"
    elif filename == 'N05':
        target = "关于科索沃战争中的暴行、军事干涉、独立申明以及其他任何与之有关的事情。"
    elif filename == 'N06':
        target = "尼泊尔统治家族（王室）事变的背景和详情以及后继的来自各方的反应。"
    elif filename == 'N07':
        target = "针对印尼华人的暴力事件。"
    elif filename == 'N08':
        target = "美国政府起诉微软垄断行为，需知道该诉讼的内容、该案例的事实、和解过程以及最后的判决。"
    elif filename == 'N09':
        target = "各国已经进行的核武器试验。"
    elif filename == 'N10':
        target = "叙利亚对中东和平进程的立场。"
    elif filename == 'N11':
        target = "美国在线（AOL）和网景（Netscape）的关系是什么？"
    elif filename == 'N12':
        target = "什么是厄尔尼诺？"
    elif filename == 'N13':
        target = "中俄之间发生的事情。"
    elif filename == 'N14':
        target = "什么是温室气体？"
    elif filename == 'N15':
        target = "北约和波兰是什么关系？"
    elif filename == 'N16':
        target = "泰国在亚洲经济危机中的角色及其对世界经济的影响，同时各国针对这次危机所采取的步骤。"
    #jieba分词
    seggen = jieba.cut_for_search(target)
    # #pkuseg分词
    # seggen = pkuseg.pkuseg().cut(target)
    #snownlp分词
    # seggen = SnowNLP(target).words
    stopwords = [line.strip() for line in open('stopwords.txt', encoding='UTF-8').readlines()]
    text_split_no = []
    for word in seggen:
        if word not in stopwords:
            text_split_no.append(word)
    text_split_no = [word.strip() for word in text_split_no if word.strip() != '']
    vectorizer = pickle.load(open("vectorizer.pickle", "rb"))
    seg_list = " ".join(text_split_no)
    seg_list = [seg_list]
    result = vectorizer.transform(seg_list)
    # print(len(vectorizer.get_feature_names()))
    # tfidf_matrix = pd.read_csv('tfidf_matrix.csv', header=None)
    tfidf_matrix = np.loadtxt("tfidf_matrix.txt")
    score_list = {}
    for i in range(len(tfidf_matrix)):
        score_list[i] = np.dot(result.toarray(), tfidf_matrix[i])
    # print(result.shape)
    # print(result.toarray())
    # np.savetxt("result.txt", result.toarray())
    # print(score_list)
    sortedlist = sorted(score_list.items(), key=lambda d: d[1], reverse=True)
    # print('得分列表', sortedlist)
    # print(score_list[43])
    cnt = 0
    cnt2 = 0  # 用于计算RECALL
    cos = []
    for num, docscore in sortedlist:
        cnt = cnt + 1
        cursor.execute('select location from `接单`.`doc_location` where doc=%s', (num + 1,))
        url = cursor.fetchall()[0][0]
        doc = url.split('\\')
        if filename in doc:
            cnt2 = cnt2 + 1
            cos.append(docscore)
        print("搜索结果" + str(cnt) + ":")
        print('文件路径：', url, '余弦相似度：', docscore)

        if cnt2 >= 25:
            break
    if cnt2 == 0:
        print('无搜索结果，请更换关键词重试')
        continue
    recall = cnt2 / a
    precision = cnt2 / 25
    # print(recall)
    # print(precision)
    try:
        print(target)
        print('\n', 'RECALL = ', recall,'\n', 'PRECISION = ', precision,'\n', 'F1 = ', 2 * precision * recall / (precision + recall))
        print(cos)

    except:
        print(precision)
        print(recall)
        print(cnt2)
        print('===========================================================')

