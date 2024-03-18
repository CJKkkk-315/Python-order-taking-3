import jieba
from snownlp import SnowNLP

import chardet
import pymysql
# import MySQLdb
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
import numpy as np
import pandas as pd
import time

# 打开数据库连接
# db = MySQLdb.connect("localhost",
#                      "root", "CYT",
#                      "search_engine",
#                      charset='utf8')
db = pymysql.connect("localhost",
                     "cjk123", "123456",
                     "接单",
                     charset='utf8')
cursor = db.cursor()
# 当已存在数据库的时候，需要将表删除，若不存在或第一次运行，则需要注释掉
cursor.execute('DROP TABLE `接单`.`doc_location`')
cursor.execute('CREATE TABLE `接单`.`doc_location` '
               '(`doc` INT NOT NULL,`location` TEXT NULL,PRIMARY KEY (`doc`))')
cursor.execute('DROP TABLE `接单`.`inverted_list`')
cursor.execute('CREATE TABLE `接单`.`inverted_list` '
               '(`term` VARCHAR(25) NOT NULL,`doc` TEXT NULL,PRIMARY KEY (`term`))')
db.commit()
db.close()
total_doc = []
total_time = 0

def Segmentation():
    global total_time
    id = 0
    for line in open("path.txt"):
        path_ = line.strip()
        id += 1
        line = line.split('\\')[-1].split('\\')[-1].split('.')[0]
        path = 'TXT' + '\\' + line + '.txt'  # path为文件位置
        fb = open(path, "rb")
        data = fb.read()
        # print(data)
        encoding = chardet.detect(data)['encoding']  # 获取文件编码
        # print(encoding)
        # page = open(path, 'r', encoding=encoding, errors='ignore').read()
        # page1=page.decode('UTF-8')
        if encoding == 'UTF-16':
            data = data.decode('UTF-16')
            data = data.encode('utf-8')
            data = data.decode('utf-8')
        else:
            data = data.decode(encoding)
        # print(chardet.detect(data)['encoding'])
        stopwords = [line.strip() for line in open('stopwords.txt', encoding='UTF-8').readlines()]

        # jieba搜索引擎分词   first1
        start_time = time.time()
        # seg_list = jieba.lcut_for_search(data)
        # seg_list = SnowNLP(data).words
        seg_list = jieba.cut(data)
        end_time = time.time()
        print('总时间为：', str(end_time - start_time))
        total_time = total_time + end_time - start_time
        # print(data)
        # #snownlp
        #
        # #pkuseg分词
        # try:
        #     print(chardet.detect(data)['encoding'])
        # except:
        #     pass
        # seg_list = pkuseg.pkuseg().cut(data)
        # #thulac分词
        # data = "".join(data)
        # print(type(data))
        # seg_list = thulac.thulac(seg_only=True).cut(data, text=True)
        text_split_no = []
        for word in seg_list:
            if word not in stopwords:
                text_split_no.append(word)
        text_split_no = [word.strip() for word in text_split_no if word.strip() != '']
        total_doc.append(text_split_no)
        # print(text_split_no)

        # db = MySQLdb.connect("localhost", "root", "CYT", "search_engine", charset='utf8')  # 创建数据库
        db = pymysql.connect("localhost",
                             "cjk123", "123456",
                             "接单",
                             charset='utf8')  # 创建数据库
        cursor = db.cursor()  # 创建游标
        cursor.execute('insert into `接单`.`doc_location` values(%s, %s)', (id, path_))
        # 对每个分出的词语建立词表
        for word in text_split_no:
            # print(word)
            # 检验看看这个词语是否已存在于数据库
            cursor.execute('select doc from `接单`.`inverted_list` where term= %s', (word,))
            result = cursor.fetchall()
            # 如果不存在
            if len(result) == 0:
                docliststr = str(id)
                cursor.execute('insert into `接单`.`inverted_list` values(%s,%s)', (word, docliststr))
            # 如果已存在
            else:
                docliststr = result[0][0]  # 得到字符串
                docliststr += ' ' + str(id)
                cursor.execute('update `接单`.`inverted_list` set doc=%s where term=%s', (docliststr, word))
        db.commit()
        db.close()


if __name__ == '__main__':
    Segmentation()
    vectorizer = TfidfVectorizer(token_pattern=r"(?u)\b\w+\b")
    total_doc = [" ".join(doc) for doc in total_doc]
    result = vectorizer.fit_transform(total_doc)
    pickle.dump(vectorizer, open("vectorizer.pickle", "wb"))
    # print(result.toarray())
    # data = pd.DataFrame(result.toarray())  # 为了能够使这组数据成为可以让pandas处理的数据，需要通过这个数组创建DataFrame。
    # data.to_csv('tfidf_matrix.csv', index=False, header=False)
    np.savetxt("tfidf_matrix.txt", result.toarray())
    # print(len(vectorizer.get_feature_names()))
    # print(vectorizer.vocabulary)
    print(total_time)