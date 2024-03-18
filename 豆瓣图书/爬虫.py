tag = {'文学':['小说','随笔','日本','文学','散文','诗歌','童话','名著','港台'],
       '流行':['漫画','推理','绘本','科幻','青春','言情','奇幻','武侠'],
       '文化':['历史','哲学','传记','设计','电影','建筑','回忆录','音乐'],
       '生活':['旅行','励志','教育','职场','美食','灵修','健康','家居'],
       '经管':['经济学','管理','商业','金融','营销','理财','股票','企业史'],
       '科技':['科普','互联网','编程','交互设计','算法','通信','神经网络']}
headers = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Cache-Control': 'max-age=0',
  'Connection': 'keep-alive',
  'Cookie': 'douban-fav-remind=1; __utmc=30149280; ll="118201"; _ga=GA1.1.491822689.1623747306; _ga_RXNMP372GL=GS1.1.1633688561.1.0.1633688563.0; __gads=ID=0c28cbccd780629c-22b2684f51cc002c:T=1623747305:RT=1633689082:S=ALNI_MYB9yVNkv8-ZUHueuIvDzAtYZKXyQ; gr_user_id=376fb970-3719-46d1-981c-a28050ebb796; dbcl2="220718836:iioDCSEhQ1c"; ck=iD5I; __utmv=30149280.22071; bid=E-70Z1NcX2k; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03=45622fb6-8575-4cff-9de0-41ac782cf250; gr_cs1_45622fb6-8575-4cff-9de0-41ac782cf250=user_id%3A0; _vwo_uuid_v2=DD9196D79AE221045B658CABC8E655B6F|046090abe7a4439c6ac2e229defc6894; __utma=30149280.491822689.1623747306.1655522701.1655781608.181; __utmz=30149280.1655781608.181.42.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=81379588.491822689.1623747306.1655781608.1655781608.1; __utmc=81379588; __utmz=81379588.1655781608.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; _pk_ref.100001.3ac3=%5B%22%22%2C%22%22%2C1655781609%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DFYINF4ZWpnyO4q96eua7bjBQTiF25ujZddaRCrzXomvUm5pzEjoE-wvnCTjvxH1-%26wd%3D%26eqid%3Df8cd039a000176e70000000562b138e3%22%5D; _pk_ses.100001.3ac3=*; gr_session_id_22c937bbd8ebd703f2d8e9445f7dfd03_45622fb6-8575-4cff-9de0-41ac782cf250=true; ap_v=0,6.0; Hm_lvt_16a14f3002af32bf3a75dfe352478639=1655781756; Hm_lpvt_16a14f3002af32bf3a75dfe352478639=1655781756; __gpi=UID=000006a6639f477d:T=1655268887:RT=1655781772:S=ALNI_Mbym3IpQSkkFpNDxM_T_J_C09Pb-Q; viewed="35776311_35196328_30293801_33450010_26381341"; __yadk_uid=oDpuHIx7yI94qzeF6DuUZgrL8kSLlTVO; __utmt_douban=1; __utmb=30149280.16.10.1655781608; __utmt=1; __utmb=81379588.13.10.1655781608; _pk_id.100001.3ac3=c4f2e8741babfb5e.1655781609.1.1655782358.1655781609.; bid=9LbP4_Sdjew',
  'Referer': 'https://book.douban.com/',
  'Sec-Fetch-Dest': 'document',
  'Sec-Fetch-Mode': 'navigate',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-User': '?1',
  'Upgrade-Insecure-Requests': '1',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36 OPR/87.0.4390.45',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Opera";v="87"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"'
}
res = []
import requests
from bs4 import BeautifulSoup
for key in tag.keys():
    for subcate in  tag[key]:
        response = requests.get('https://book.douban.com/tag/'+subcate + '?start=20&type=T',headers=headers)
        soup = BeautifulSoup(response.text)
        for i in soup.find(class_='subject-list').find_all(name='li'):
            try:
                name = i.find(name='h2').find(name='a').text.replace('\n','').replace(' ','')
                l = i.find(class_='pub').text.replace('\n','').replace(' ','').split('/')
                writer = l[0]
                price = l[-1]
                time = l[-2]
                p = l[-3]
                score = i.find(class_='rating_nums').text.replace('\n','').replace(' ','')
                hot = i.find(class_='pl').text.replace('\n','').replace(' ','')
                content = i.find(name='p').text.replace('\n','').replace(' ','')
                res.append([name,key,subcate,writer,price,time,p,score,hot,content])
                print([name,key,subcate,writer,price,time,p,score,hot,content])
            except:
                continue
import csv
with open('res.csv','a+',newline='',encoding='utf8') as f:
    fcsv = csv.writer(f)
    for i in res:
        fcsv.writerow(i)