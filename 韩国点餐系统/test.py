import time
import datetime
import random
def get_now_time():
    now = time.localtime()
    now_time = time.strftime("%Y-%m-%d", now)
    return now_time
date1 = get_now_time()
for i in range(20):
    d = (datetime.datetime.strptime(date1,"%Y-%m-%d")-datetime.timedelta(days=i)).strftime("%Y-%m-%d")
    with open('record.csv', 'a+', encoding='utf8', newline='') as f:
        f.write(f'双层牛肉堡,{random.randint(1,10)},{d}\n')
        f.write(f'单层鳕鱼堡,{random.randint(1,10)},{d}\n')
        f.write(f'薯条,{random.randint(1,10)},{d}\n')
        f.write(f'可乐,{random.randint(1,10)},{d}\n')
    # date2 = datetime.strptime(i[-2], "%Y%m%d")
    # duration = date1 - date2
    # day = duration.days