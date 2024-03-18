from  selenium import webdriver
import time
import excel
from lxml import etree
import requests
from aip import AipOcr
excel_src = r'D:\PYTHON接单3\zifu.xlsx'
chrome_src = r'D:\PYTHON接单\智联天机\chromedriver.exe'  # 自动化游览器路径


def error_Grab():
    url = 'https://gz.shuatiw.com/index.php?exam-app-point&questype=&pointid=665&number=1'
    lista = [['问题', '回答', '答案', '解答', '科目']]  # 设置一个空的列表 方便写入excel
    for raa in range(1, 9):
        # msql = MSSQL('.','sa','mrsoft','xuewenhao')   #链接数据库 自己写的一个Python链接数据库的方法

        wb = webdriver.Chrome(chrome_src) #打开游览器
        wb.maximize_window()  #游览器i最大化
        wb.get(url)
        time.sleep(2) #访问网站后设置等待时间 防止错误和加载某些时间ajex
        #####一下是登陆设置
        wb.find_element_by_xpath('/html/body/font/div[1]/div/div/div/div[2]/form/div[1]/input').click()
        time.sleep(0.3)  #等待  为了防止点击未加载出来
        wb.find_element_by_xpath('/html/body/font/div[1]/div/div/div/div[2]/form/div[1]/input').send_keys('854239312')
        wb.find_element_by_xpath('/html/body/font/div[1]/div/div/div/div[2]/form/div[2]/input').click()
        time.sleep(0.1)#等待  为了防止点击未加载出来
        wb.find_element_by_xpath('/html/body/font/div[1]/div/div/div/div[2]/form/div[2]/input').send_keys('asasas123')
        time.sleep(0.2)#等待  为了防止点击未加载出来
        wb.find_element_by_xpath('/html/body/font/div[1]/div/div/div/div[2]/form/div[3]/p/button').click()
        time.sleep(2)#等待  为了防止点击未加载出来
        ippa = 0
        #########################
        ippa+=1
        ippastr = str(ippa)
        try:
            rea = str(raa)
            xpaaa = '//div[@class="col-xs-3"]['+rea+']'
            subject = ''
            wb.find_element_by_xpath(xpaaa).click() ##定位  下一个科目的定位   化学,生物....
        except:
           print('这有问题-----')
        time.sleep(0.8)
        subject1 = wb.find_element_by_xpath('/html/body/div[3]/div/div/div/div/h1').text

        subject = subject1
        wb.find_element_by_xpath('/html/body/div[3]/div/div/div/div/div/a[1]').click()
        time.sleep(1)
        wb.find_element_by_xpath('//*[@id="panel-element-1"]/ul/li[1]/a[2]').click()
        time.sleep(0.9)
        ipd = 0
        for in23 in range(1,30):   ###循环 没次做30个题
            ipd+=1
            ipdstr = str(ipd)

            wb.find_element_by_xpath('//*[@id="selectbox"]/div/div[1]/label/span').click()
            #/html/body/div[4]/div/div/div/div/div/div[1]/a
            #/html/body/div[3]/div/div/div/div/div/a[1]
            #//*[@id="panel-element-1"]/ul/li[1]/a[2]



            ## 第一个标题/html/body/div[3]/div/div/div[2]/div[2]/div[2]/div
            #点击//*[@id="selectbox"]/div/div[1]/label/span
            #我的大难 //*[@id="answerbox"]/div[2]/text()[1]
            #参考答案//*[@id="answerbox"]/div[3]/text()[1]

            ###---------------------------------------
            ####提取信息
            htmltext = wb.execute_script("return document.documentElement.outerHTML")
            html = etree.HTML(htmltext)
            Title = html.xpath('/html/body/div[3]/div/div/div[2]/div[2]/div[2]/div/text()')
            if Title:  ###题
                Title = Title[0].replace('\n','').replace(' ','')
                imagetitle = Title.replace('(','').replace(')','').replace(',','').replace(' ','').replace('（','').replace('）','').replace('。','').replace('：','').replace('|','').replace('、','').replace('”','').replace('？','').replace('、','').replace('/','').replace('，','').replace('，按5元/月全球标准收取','').replace('取而代之对短信按流量收费假设每月流量30M','').replace('。','')
            else:
                Title = ''

            answer = html.xpath('//*[@id="answerbox"]/div[2]/span/text()')
            if answer :
                answer = answer[0].replace('\n','').replace(' ','')
            else:
                answer = ''
            answer_true = html.xpath('//*[@id="answerbox"]/div[3]/span/text()')
            if answer_true :
                answer_true = answer_true[0].replace('\n','').replace(' ','')
            else:
                answer_true = ''
            url_one = html.xpath('//*[@id="answerbox"]/div[5]/p/img/@src')   ##获取图片的src属性
            url_one =url_one[0].replace('\n','').replace(' ','')
            url_two = r'https://gz.shuatiw.com/'+url_one
            print(url_two)
            ppp = url_one.split('.')[-1]
            image = requests.get(url_two).content
            # print(image)
            srca = 'D:\PYTHON接单3\图片\\'+ippastr+ipdstr+imagetitle+'.'+ppp   #存png路径
            # if not os.path.exists(srca):
            #     os.mkdir(srca)
            try:
                with open(srca,'wb') as wei:
                    wei.write(image)
            except:
                print('图片下载失败')
                pass
            # im = Image.open(srca)
            # text = pytesseract.image_to_string(im)
            # print(text)
            # print(image)

            #####调用百度api
            api_key = 'pZvzeeqTwMp7hm9int772Zp5'
            selc_kfc = 'UevP51NxF3BsZGq8DSA6QHEFZtmtj2F5'
            client = AipOcr('24306649', api_key, selc_kfc)
            res = client.basicGeneral(image)
            print(res)   # 图片识别结果json
            aeea = ''
            try:
                for key, values in res.items():
                    key_w = 'words_result'
                    if key == key_w:
                        values1 = values

                    for re in values1:
                        for key, values in re.items():
                            values_zuizhong = values
                            aeea = aeea + values_zuizhong
            except:
                print('图片识别失败')
                aeea = ''
                pass

            ###整理数据
            jiexi = aeea.replace('\n','').replace('】','')  ###写入excel
            lista1 = [Title,answer,answer_true,jiexi,subject]
            lista.append(lista1)
            time.sleep(0.5)
            ###往sql server数据库插入数据
            # try:
            #     insert = "insert into [xuewenhao].[dbo].[cuoti] ([url],[col1],[col2],[col3],[col4],col5)  VALUES (%s,%s,%s,%s,%s,%s) "
            #     msql.ExecNonQuery(insert,(url_two,Title,answer,answer_true,jiexi,subject))
            #     print('插入成功')
            # except Exception as wewewe :
            #     print(str(wewewe))
            #     print('插入失败')
            #     pass

            try:
                wb.find_element_by_xpath('/html/body/div[3]/div/div/div[2]/div[2]/div[1]/a[3]').click()   #点击下一题
                time.sleep(2)
                print(in23)
            except Exception as aaaaadd:

                pass
        wb.close()
    print(lista)
    excel.excel_copy(excel_src,'Sheet','A1',lista)
if __name__ == '__main__':
    error_Grab()
