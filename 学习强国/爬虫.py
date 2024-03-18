import time
res = []
from selenium import webdriver
# 初始化浏览器驱动器
driver = webdriver.Chrome(executable_path='D:\PYTHON接单\智联天机\chromedriver.exe',options=option)
# 打开目标网址
driver.get('https://www.xuexi.cn/5c90534c80d14c060d6683fa960e3676/82573c005c024095037d2186a02244cb.html')
time.sleep(3)
# 循环遍历20个所有链接
for i in range(1,21):
    # 记录当前页面
    allHandles1 = driver.window_handles
    # 点击新页面
    driver.find_element_by_xpath(f'//*[@id="d480"]/div/div/div/div/div/section/div/div/div[1]/div/div[{i}]/div/div/div/span').click()
    # 切换到新页面
    allHandles2 = driver.window_handles
    newhandle = [handle for handle in allHandles2 if handle not in allHandles1]
    driver.switch_to.window(newhandle[0])
    time.sleep(3)
    # 同样循环所有链接
    for j in range(1, 21):
        # 嵌套点击， 与上述原理相同
        try:
            allHandles3 = driver.window_handles
            driver.find_element_by_xpath(f'//*[@id="page-main"]/section/div/div/div/div/div/section/div/div/div/div[1]/div/section/div/div/div/div/div/section/div/div/div/div/div[3]/section/div/div/div/div/div/section/div/div/div/div/div[{j}]/div/div/div[1]/span').click()
            allHandles4 = driver.window_handles
            newhandle1 = [handle for handle in allHandles4 if handle not in allHandles3]
            driver.switch_to.window(newhandle1[0])
            time.sleep(3)
            text = driver.find_element_by_xpath('//*[@id="root"]/div/section/div/div/div/div/div[2]/section/div/div/div/div/div/div/div[3]').text
            res.append(text)
            driver.close()
            driver.switch_to.window(newhandle[0])
        except:
            break
    driver.close()
    driver.switch_to.window(allHandles1[0])
# 将爬取到的所有文件写入txt中
with open('data.txt','w',encoding='utf-8') as f:
    for i in res:
        f.write(i+'\n')