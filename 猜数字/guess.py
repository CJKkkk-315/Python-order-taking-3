import random
# 使用随机库生成4位数字
ans = ''.join([str(random.randint(0,9)) for _ in range(4)])
# 不断循环读入用户输入
while True:
    try:
        guess = input('请输入四位数字：')
        # 特殊命令search，直接输出答案
        if guess == 'search':
            print(ans)
            continue
        # 特殊命令change，直接修改答案
        elif guess == 'change':
            ans = input('请输入新四位数字：')
            continue
        # 特殊命令restart，随机重置答案
        elif guess == 'restart':
            ans = ''.join([str(random.randint(0, 9)) for _ in range(4)])
            continue
        a = 0
        b = 0
        # 遍历输入的4个数字
        for i in range(4):
            # 如果位置和数字都对，a+1
            if guess[i] == ans[i]:
                a += 1
            # 如果位置不对但数字对，b+1
            elif guess[i] in ans:
                b += 1
        # 输出ab结果
        print(f'A{a}B{b}')
        # 若4个都猜对，结束游戏
        if a == 4:
            break
    # 若检测到输入异常，提示输入错误
    except:
        print('输入错误！')
