import requests
from bs4 import BeautifulSoup
rows1 = []
rows2 = []
for page in range(1,167):
    res = requests.get(f'http://172.19.163.200:5003/GetIds?stdid=2104010203&page={page}')
    soup = BeautifulSoup(res.text)
    for i in soup.find(name='tbody').find_all(name='tr'):
        row = [j.text.replace(' ','') for j in i.find_all(name='td')]
        rows1.append(row)
    print(1)
for page in range(1,293):
    res = requests.get(f'http://172.19.163.200:5003/GetIds?stdid=2102030114&page={page}')
    soup = BeautifulSoup(res.text)
    for i in soup.find(name='tbody').find_all(name='tr'):
        row = [j.text.replace(' ','') for j in i.find_all(name='td')]
        rows2.append(row)
    print(1)
with open('data1.txt','w',encoding='utf8') as f:
    for i in rows1:
        f.write(','.join(i)+'\n')
with open('data2.txt','w',encoding='utf8') as f:
    for i in rows2:
        f.write(','.join(i)+'\n')