import requests
from bs4 import BeautifulSoup
import csv

res = []
for page in range(1,7):
    response = requests.get(f'https://xww.cqwu.edu.cn/channel_23133_03{str(page)}.html')
    soup = BeautifulSoup(response.text)
    for i in soup.find(class_='list-group').find_all(name='a')[:15]:
        name = i.text
        l = [i for i in name.replace(' ','').replace('\t','').split('\n') if i]
        name = l[0]
        time = l[1]
        href = i.get('href')
        soup1 = BeautifulSoup(requests.get(href).text)
        try:
            f = soup1.find(class_='news-date').text.split('来源：')[1].replace('\n','').replace(' ','')
            url2 = 'https://www.cqwu.edu.cn/visitcount.html?articleid=' + href.replace('.html', '').split('_')[1]
            soup2 = requests.get(url2).text
            c = soup2.split('\'')[1]
        except:
            f = soup1.find(class_='abs').find_all(name='span')[1].text.replace('作者：','')
            url2 = 'https://dsxx.cqwu.edu.cn/visitcount.html?articleid=' + href.replace('.html', '').split('_')[1]
            soup2 = requests.get(url2).text
            c = soup2.split('\'')[1]
        res.append([name,time,href,f,c])
with open('data1.csv','w',newline='',encoding='utf-8') as f:
    fcsv = csv.writer(f)
    for i in res:
        fcsv.writerow(i)

