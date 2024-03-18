class Student:
    def __init__(self,uid,name,age):
        self.age = age
        self.uid = uid
        self.name = name
    def intro(self):
        print(f'学生姓名：{self.name} 学号为：{self.uid} 年龄为：{self.age}')
while True:
    username = input('请输入账号：')
    password = input('请输入密码：')
    if username == '123456' and password == '123456':
        print('登陆成功')
        break
    else:
        print('登录失败')
uid = input('请输入学生学号：')
name = input('请输入学生姓名：')
age = input('请输入学生年龄：')
student = Student(uid,name,age)
student.intro()
