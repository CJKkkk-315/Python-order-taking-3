import os
# 定义最后排序完成的总列表
ans = []
# 遍历所有文件夹
for ch in 'abcdefghijklmnopqrstuvwxyz':
    # 定义每个文件夹里所有数据的总列表
    data = []
    filelist = os.listdir(f'tempFile/{ch}')
    # 遍历每个文件夹里的每个文件
    for file in filelist:
        # 打开文件，将文件内容作为列表写入data中
        with open(f'tempFile/{ch}/{file}') as f:
            data.append([i.replace('\n','') for i in f.readlines()])
    # 定义每个文件夹里排序好后的总列表
    res = []
    # 10路归并，只要任意一路还有元素，就继续
    while True:
        target = ''
        flag = -1
        # 遍历10路元素，找出最大元素
        for i in range(10):
            if data[i]:
                if data[i][0] > target:
                    target = data[i][0]
                    flag = i
        # 若最大元素存在
        if flag != -1:
            # 则将其写入res末尾，并且删除
            res.append(target)
            del data[flag][0]
        # 若没有任何元素，则归并完成，退出
        else:
            break
    # 由于文件夹之间本身有序，将归并后的列表直接追加在ans末尾
    ans += res
# 26个文件夹全部归并完毕以后获得总数据排序列表ans，写入最终文件
with open('result.txt','w') as f:
    for i in ans:
        f.write(i+'\n')
