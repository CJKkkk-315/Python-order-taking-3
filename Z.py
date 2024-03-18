import time
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import ming
"""
从网上爬取数据的代码；
"""
# 中文处理
matplotlib.rcParams['font.family'] = ['Microsoft YaHei']
exp = [0.05, 0.01, 0.03, 0.01, 0.01, 0.25, 0]
names = ('安必平', '悦康药业', '吉贝尔', '华光新材', '之江生物','菜尔科技', '思林杰')
values = (139.67, 42.14, 175.02, 71.13, 47, 125.38, 51.81)
cls = ['#F5DEB3', '#87CEFA', '#FFB6C1', '#90EE90', '#D3D3D3', 'orange', 'pink']
plt.pie(values, explode=exp, colors=cls,autopct='%.3f%%', labels=names)
plt.title('若干家上市公司的市值及所占市场比例', fontsize=15)
plt.show()