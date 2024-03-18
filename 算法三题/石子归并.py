tone = eval(input())
cost = 0
# 直到合并成一堆石子为止
while len(tone) != 1:
    mini = sum(tone[0:2])
    n = 0
    # 循环所有石子，比较两两合并的花费代价，找出花费最小的一对石子
    for i in range(len(tone)-1):
        t = sum(tone[i:i+2])
        if t <= mini:
            mini = t
            n = i
    # 合并这两堆石子
    del tone[n]
    del tone[n]
    tone.insert(n,mini)
    # 添加合并花费
    cost += mini
print(cost)