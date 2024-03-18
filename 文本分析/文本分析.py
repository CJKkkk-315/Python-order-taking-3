import snownlp
import jieba
import matplotlib.pyplot as plt
import numpy
from PIL import Image
plt.rcParams['font.sans-serif'] = ['SimHei']
import wordcloud
from collections import Counter
data = ''.join([i.replace('\n','') for i in open('新能源.txt','r',encoding='utf8').readlines()]).replace('\t','').replace('\u3000','')
object_list = []
seg_list_exact = jieba.cut(data, cut_all=False, HMM=True)
with open('stopwords.txt', 'r', encoding='UTF-8') as meaninglessFile:
    stopwords = set(meaninglessFile.read().split('\n'))
stopwords.add(' ')
for word in seg_list_exact:
    if word not in stopwords:
        object_list.append(word)
n = len(object_list)
object_list = Counter(object_list)
mask = numpy.array(Image.open('heart.png'))
wc = wordcloud.WordCloud(
    font_path = 'C:/Windows/Fonts/simfang.ttf',
    background_color='white',
    mask=mask,
    max_words = 500,
    max_font_size = 120
)
wc.generate_from_frequencies(object_list)
plt.figure('词频比重词云')
plt.imshow(wc, cmap=plt.cm.gray, interpolation='bilinear')
plt.show()
csv_data = sorted(object_list.items(),key=lambda x:x[1],reverse=True)
with open('res.csv','w',encoding='utf8',newline='') as f:
    f.write(f'词项,比重\n')
    for i in csv_data:
        f.write(f'{i[0]},{i[1]*1000/n}\n')
s = [0,0,0]
bad = {}
mid = {}
good = {}
for i in object_list.keys():
    if snownlp.SnowNLP(i).sentiments < 0.1:
        bad[i] = object_list[i]
        s[0] += 1
    elif snownlp.SnowNLP(i).sentiments > 0.9:
        good[i] = object_list[i]
        s[2] += 1
    else:
        mid[i] = object_list[i]
        s[1] += 1
wc.generate_from_frequencies(bad)
plt.figure('负面词词云')
plt.imshow(wc, cmap=plt.cm.gray, interpolation='bilinear')
plt.show()
wc.generate_from_frequencies(mid)
plt.figure('中性词词云')
plt.imshow(wc, cmap=plt.cm.gray, interpolation='bilinear')
plt.show()
wc.generate_from_frequencies(good)
plt.figure('正面词词云')
plt.imshow(wc, cmap=plt.cm.gray, interpolation='bilinear')
plt.show()
plt.bar(['负面','中性','正面'],s)
plt.show()