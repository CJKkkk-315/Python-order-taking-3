import requests
from bs4 import BeautifulSoup
data = []
# 分别爬取两个账号所有数据
for page in range(1,130):
    res = requests.get('http://172.19.163.200:5003/GetIds?stdid=2102030119&page='+str(page))
    soup = BeautifulSoup(res.text)
    for item in soup.find(name='tbody').find_all(name='tr'):
        aw = []
        for info in item.find_all(name='td'):
            aw.append(info.text.replace(' ',''))
        data.append(aw)
for page in range(1,89):
    res = requests.get('http://172.19.163.200:5003/GetIds?stdid=2102030124&page='+str(page))
    soup = BeautifulSoup(res.text)
    for item in soup.find(name='tbody').find_all(name='tr'):
        aw = []
        for info in item.find_all(name='td'):
            aw.append(info.text.replace(' ',''))
        data.append([aw[0],aw[4],'',aw[2],aw[3],aw[6],'',aw[1]])
    print(1)
# 写入文件中
with open('origin_data.txt','w',encoding='utf8') as f:
    for i in data:
        f.write(','.join(i)+'\n')