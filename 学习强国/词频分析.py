import jieba
from collections import Counter
import matplotlib.pyplot as plt
# 设置中文字体防止中文乱码
plt.rcParams['font.sans-serif'] = ['SimHei']
res = ''
# 打开爬取好的内容
with open('content.txt','r',encoding='utf8') as f:
    data = ''.join(f.readlines())
# 去掉非中文
for ch in data:
    if '\u4e00' <= ch <= '\u9fff':
        res += ch
words = []
# 利用jieba进行分词
seg_list_exact = jieba.cut(res, cut_all=False, HMM=True)
with open('stopwords.txt', 'r', encoding='UTF-8') as meaninglessFile:
    stopwords = set(meaninglessFile.read().split('\n'))
stopwords.add(' ')
# 去除停用词
for word in seg_list_exact:
    if word not in stopwords:
        words.append(word)
# 统计词频
words = Counter(words)
# 按照词频排序
words = sorted(words.items(),key=lambda x:x[1],reverse=True)
x = []
y = []
# 筛选前10
for i in words[:10]:
    x.append(i[0])
    y.append(i[1])
# 画图
plt.bar(x,y)
plt.title('词频排名')
plt.show()