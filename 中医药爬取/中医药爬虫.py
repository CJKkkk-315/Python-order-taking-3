import requests
from bs4 import BeautifulSoup
import os
res = []

def content_get(url,cate):

    payload={}
    headers = {
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
      'Accept-Language': 'zh-CN,zh;q=0.9',
      'Cache-Control': 'max-age=0',
      'Connection': 'keep-alive',
      'Cookie': '__51cke__=; Hm_lvt_64cd3aa420eb69d437a41b84172cd0c1=1655797712; __tins__19544285=%7B%22sid%22%3A%201655797711674%2C%20%22vd%22%3A%2022%2C%20%22expires%22%3A%201655800560643%7D; __51laig__=22; Hm_lpvt_64cd3aa420eb69d437a41b84172cd0c1=1655798761',
      'Upgrade-Insecure-Requests': '1',
      'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36 OPR/87.0.4390.45'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    soup = BeautifulSoup(response.content)
    try:
        title = soup.find(class_='title').text
        with open(cate+'/'+title+'.txt','w',encoding='utf8') as f:
            try:
                f.write(soup.find(name='table').find(name='table').find(name='table').text.replace('\n','').replace(' ',''))
            except:
                f.write(soup.find(class_='content').find('table').text.replace('\n','').replace(' ',''))
    except:
        print(url)

response = requests.get('http://www.piccc.com/piccc/html/mifang/')
soup = BeautifulSoup(response.content)
for i in soup.find(class_='new_lanmu_l').find_all(class_='new_lanmu_list_cnt2 clearfix'):
    url0 = 'http://www.piccc.com/' + i.find(class_='lanmu_title').find(name='a')['href']
    cate = i.find(class_='lanmu_title').find(name='a').text
    os.mkdir(cate)
    response = requests.get(url0)
    soup = BeautifulSoup(response.text)
    for ul in soup.find(class_='chunlist').find_all(name='ul'):
        for li in ul.find_all(name='li'):
            url = 'http://www.piccc.com/' + li.find(name='a')['href']
            content_get(url,cate)



