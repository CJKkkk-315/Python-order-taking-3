import requests
from bs4 import BeautifulSoup
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36 OPR/87.0.4390.45'
}
def get_item(url):
    try:
        res = requests.get(url,headers=headers)
        soup = BeautifulSoup(res.content)
        name = soup.find(class_='huohao').text.replace('\n','').replace(' ','')
        sub_name = soup.find(class_='promise').text.replace('\n','').replace(' ','')
        category = soup.find(class_='category').find_all(name='span')[0].text.replace('\n','').replace(' ','')
        huoyuan = soup.find(class_='category').find_all(name='span')[1].text.replace('\n','').replace(' ','')
        time = soup.find(class_='starting_time').text.replace('\n','').replace(' ','')
        info = soup.find(id='propshowbox').text.replace('\n','')
        value = ';;;'.join([i.text.replace('\n',' ').replace(' ','') for i in soup.find(class_='site_right').find_all(name='div')])
        imgs = [i.find(name='img')['src'] for i in soup.find(id='thumblist').find_all(name='li')]
        print(name)
    except:
        print(url)
def get_shop(url):
    head = 'http://shop5275.bao66.cn/index.html'
    res = requests.get(head, headers=headers)
    soup = BeautifulSoup(res.content)
    page = int(soup.find(class_='pageList').find_all(name='li')[-1].text)
    for p in range(1,page+1):
        url = head.replace('index.html','') + f'all,{p},0.html'
        res = requests.get(url, headers=headers)
        soup = BeautifulSoup(res.content)
        for item in soup.find(class_='product_menu').find_all(name='li')[:5]:
            url0 = item.find(name='a')['href']
            get_item(url0)
get_shop(1)