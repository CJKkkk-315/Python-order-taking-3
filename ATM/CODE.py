username = input('请输入用户名：')
while True:
    password = input('请输入密码：')
    if len(password) >= 12:
        password1 = input('请再次输入密码：')
        if password == password1:
            print('注册成功！')
            break
        else:
            print('两次密码输入不一致，请重新输入密码')
    else:
        print('输入的密码不足12位！')
