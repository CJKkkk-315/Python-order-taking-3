import requests
from bs4 import BeautifulSoup
response = requests.get('https://www.shicimingju.com/chaxun/zuozhe/666_1.html')
response.encoding='utf-8'
soup = BeautifulSoup(response.text)
name = soup.find(class_='card about_zuozhe').find(name='h4').text
intro = soup.find(class_='des').text
f = open('data2.txt','w')
f.write(name+'\n')
f.write(intro+'\n')
for i in range(1,6):
    response = requests.get('https://www.shicimingju.com/chaxun/zuozhe/666_{}.html'.format(str(i)))
    response.encoding='utf-8'
    soup = BeautifulSoup(response.text)
    for i in soup.find_all(class_='shici_list_main'):
        title = i.find(name='h3').text
        content = i.find(class_='shici_content').text.replace('展开全文','').replace('收起','')
        f.write(title+'\n')
        f.write(content+'\n')
f.close()
