people = eval(input('people = '))
limit = eval(input('limit = '))
res = []
# 先对人按照体重升序排序
people.sort(reverse=True)
# 只要还有人没上船就继续
while people:
    # 最重的人上船
    p1 = people[0]
    # 如果有人单人无法上船，直接打印失败
    if p1 > limit:
        print('无法搭载')
        break
    # 最重的人先上传
    people.remove(p1)
    # target为船上剩余重量
    target = limit - p1
    # 从剩下的人中找到满足剩余重量且重量最大的
    p2 = None
    for i in people:
        if i <= target:
            p2 = i
            break
    # 若有 则上船
    if p2:
        people.remove(p2)
        res.append([p1,p2])
    # 没有 则那个人单独上船
    else:
        res.append([p1])
# 打印一共几条船
print(len(res))



