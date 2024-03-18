from tkinter import *
import tkinter as tk
import tkinter.messagebox
import random
from datetime import *
import time
# 获取当前时间函数
def get_now_time():
    now =  time.localtime()
    # 格式精确到秒
    now_time = time.strftime("%Y-%m-%d-%H:%M:%S", now)
    return now_time
# 读取谜语文件，将谜语和谜底添加到列表中
with open('data.txt',encoding='utf8') as f:
    mystery = [i.replace('\n','').split() for i in f.readlines()]
# 读取用户文件，将当前经验添加exp变量中 将历史记录添加到列表中
with open('user.txt',encoding='utf8') as f:
    data = f.readlines()
    exp = int([i.replace('\n','') for i in data][0])
    record = [i.replace('\n','').split() for i in data[1:]]
# f1为答题功能
def f1():
    global l0
    # 初始分数为0
    score = 0
    # 定义返回主菜单函数，关闭当前界面，显示主界面
    def back():
        root2.destroy()
        root1.deiconify()
    # 定义提交答案函数
    def flash():
        global exp
        nonlocal score
        # 判断用户提交答案和谜底是否相同
        if e.get() == q[0][1]:
            # 相同则分数加一
            tk.messagebox.showinfo(message='猜对啦！')
            score += 1
        else:
            tk.messagebox.showinfo(message='猜错啦！')
        # 删掉答过的谜题
        del q[0]
        # 如果题目列表还有题目
        if q:
            # 刷新谜面
            l.config(text=q[0][0])
        # 如果所有题目都答完了
        else:
            # 给出最终得分
            tk.messagebox.showinfo(message=f'你的最终得分为{score}')
            # 刷新经验和等级
            exp += score
            record.append([get_now_time(),str(score)])
            l0.config(text=f'当前等级：Lv{exp // 10 + 1}')
            # 返回主界面
            root2.destroy()
            root1.deiconify()
    # 进入答题函数 随机从谜语列表抽取10道题
    q = random.sample(mystery,10)
    # 隐藏主窗口
    root1.withdraw()
    # 打开答题窗口
    root2 = Tk()
    root2.title('猜谜语小游戏')
    root2.geometry("300x200")
    # 定义计时函数
    def foo():
        global timm
        # 每1000毫秒刷新一次
        time_lable.after(1000, foo)
        timm = timm - 1
        # 若时间用完则提示失败
        if timm == 0:
            tk.messagebox.showinfo(message='超时！挑战失败！')
            root2.destroy()
            root1.deiconify()
        else:
            time_lable['text'] = '倒计时:' + str(timm)
    global timm
    timm=100
    time_lable = tkinter.Label(root2, text='倒计时:' + str(timm))
    time_lable.pack()
    time_lable.after(1000, foo)
    # 设置谜面和谜底输入框
    Label(root2, text='谜面为：').pack()
    l = Label(root2, text=q[0][0])
    l.pack()
    Label(root2, text='请输入谜底：').pack()
    e = Entry(root2, width=70)
    e.pack()
    Button(root2, text='提交', command=flash).pack()
    Label(root2, text='').pack()
    Button(root2, text='返回', command=back).pack()
    root2.mainloop()
# 定义历史记录功能
def f2():

    root2 = Toplevel(root1)
    root2.title('猜谜语小游戏')
    root2.geometry("300x580")
    # 循环展示所有记录
    for i in record:
        Label(root2, text=f"时间：{i[0]}   得分：{i[1]}").pack()
# 主窗口
root1 = Tk()
root1.title('猜谜语小游戏')
root1.geometry("300x140")
# 显示等级
l0 = Label(root1,text=f'当前等级：Lv{exp//10+1}')
l0.place(x=0,y=0)
Label(root1,text='').pack()
# 定义按钮
Button(root1, text='开始猜谜', command=f1,width=15).pack()
Label(root1,text='').pack()
Button(root1, text='查看历史记录', command=f2,width=15).pack()
root1.mainloop()
# 程序结束时 将新的用户信息写入文件
with open('user.txt','w',encoding='utf8') as f:
    f.write(str(exp)+'\n')
    for i in record:
        f.write(' '.join(i)+'\n')