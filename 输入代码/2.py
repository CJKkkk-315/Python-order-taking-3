import csv
import random
import datetime

fn = 'data.csv'

with open(fn, 'w') as fp:
    # 创建csv文件写入对象
    wr = csv.writer(fp,lineterminator='\n')
    # 写入表头
    wr.writerow(['日期', '销量'])

    # 生成模拟数据
    startDate = datetime.date(2017, 1, 1)

    # 生成365个模拟数据，可以根据需要进行调整
    for i in range(365):
        # 生成一个模拟数据，写入csv文件
        amount = 300 + i*5 + random.randrange(100)
        wr.writerow([str(startDate), amount])
        # 下一天
        startDate = startDate + datetime.timedelta(days=1)
