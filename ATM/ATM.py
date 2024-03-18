import random
# 初始化随机余额
number = random.randint(100,1000)
# 初始化正确的pin
right_pin = '1234'
# 错误次数
n = 0
while True:
    # 若错误次数达到3次
    if n == 3:
        print('错误次数超过3次，请重启！')
        # 程序进入死循环
        while True:
            pass
    # 用户输入pin
    pin = input('请输入4位pin:')
    # 若pin不为4位，则提示出错
    if len(pin) != 4:
        print('输入位数有误！')
        n += 1
    # 若pin正确，则提示成功并break跳出循环
    elif pin == right_pin:
        print('登陆成功！')
        break
    # 若pin错误，则继续循环
    else:
        print('pin错误！')
        n += 1
# 菜单
info = """
1. 检查余额
2. 提取资金
3. 存入账户
4. 退出
"""
while True:
    # 打印菜单
    print(info)
    # 读取用户输入
    c = input('请输入你的选择（1/2/3/4）：')
    # 若为1，则打印余额
    if c == '1':
        print('当前余额为：' + str(number))
    # 若为2 则进行提取资金
    elif c == '2':
        # 检查输入是否为数字
        try:
            m = float(input('请输入要提取的金额：'))
            # 检查余额是否充足
            if m > number:
                print('余额不足')
            else:
                # 扣除余额
                number = number - m
                print('提取成功！')
        # 若不为数字，则提示出错
        except:
            print('请输入正确的金额！')
    # 若为3 则进行存入资金
    elif c == '3':
        # 检查输入是否为数字
        try:
            m = float(input('请输入要粗存入的金额：'))
            # 添加资金，提示成功
            number = number + m
            print('存入成功！')
        # 若不为数字，则提示出错
        except:
            print('请输入正确的金额！')
    elif c == '4':
        break
    else:
        print('请输入正确的选项')
