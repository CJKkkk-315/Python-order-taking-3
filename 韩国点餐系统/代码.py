from tkinter import *
import tkinter as tk
import tkinter.messagebox
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
import time
import datetime
# 获取今日时间
def get_now_time():
    now = time.localtime()
    now_time = time.strftime("%Y-%m-%d", now)
    return now_time
# 计算总销量
def count_all():
    d = {}
    data = [i.replace('\n','').split(',') for i in open('record.csv',encoding='utf8').readlines()]
    for i in data:
        d[i[0]] = d.get(i[0],0) + int(i[1])
    xy = list(d.items())
    x = [i[0] for i in xy]
    y = [i[1] for i in xy]
    plt.bar(x,y)
    plt.show()
# 近7天柱状图
def count_bar():
    d = {'双层牛肉堡': [0 for _ in range(7)], '单层鳕鱼堡': [0 for _ in range(7)], '薯条': [0 for _ in range(7)], '可乐': [0 for _ in range(7)]}
    encode = {(datetime.datetime.strptime(get_now_time(), "%Y-%m-%d") - datetime.timedelta(days=i)).strftime("%Y-%m-%d"):i for i in range(7)}
    data = [i.replace('\n', '').split(',') for i in open('record.csv', encoding='utf8').readlines()]
    for i in data:
        if i[2] in encode:
            d[i[0]][encode[i[2]]] += int(i[1])
    labels = [(datetime.datetime.strptime(get_now_time(), "%Y-%m-%d") - datetime.timedelta(days=i)).strftime("%Y-%m-%d") for i in range(7)]
    labels = labels[::-1]
    x1 = [1, 4, 7, 10, 13,16,19]
    x2 = [1.5, 4.5, 7.5, 10.5, 13.5,16.5,19.5]
    x3 = [2, 5, 8, 11, 14,17,20]
    x4 = [2.5, 5.5, 8.5, 11.5, 14.5,17.5,20.5]
    plt.bar(x1, d['双层牛肉堡'][::-1],width=0.5,label='双层牛肉堡')
    plt.bar(x2, d['单层鳕鱼堡'][::-1],width=0.5,label='单层鳕鱼堡')
    plt.bar(x3, d['薯条'][::-1], width=0.5, label='薯条')
    plt.bar(x4, d['可乐'][::-1], width=0.5, label='可乐')
    plt.xticks(x3,labels)
    plt.tick_params(axis='x',bottom=False)
    plt.legend()
    plt.show()
# 近7天折线图
def count_line():
    d = {'双层牛肉堡': [0 for _ in range(7)], '单层鳕鱼堡': [0 for _ in range(7)], '薯条': [0 for _ in range(7)],
         '可乐': [0 for _ in range(7)]}
    encode = {
        (datetime.datetime.strptime(get_now_time(), "%Y-%m-%d") - datetime.timedelta(days=i)).strftime("%Y-%m-%d"): i
        for i in range(7)}
    data = [i.replace('\n', '').split(',') for i in open('record.csv', encoding='utf8').readlines()]
    for i in data:
        if i[2] in encode:
            d[i[0]][encode[i[2]]] += int(i[1])
    labels = [(datetime.datetime.strptime(get_now_time(), "%Y-%m-%d") - datetime.timedelta(days=i)).strftime("%Y-%m-%d")
              for i in range(7)]
    labels = labels[::-1]
    plt.plot(labels, d['双层牛肉堡'][::-1],label='双层牛肉堡')
    plt.plot(labels, d['单层鳕鱼堡'][::-1],  label='单层鳕鱼堡')
    plt.plot(labels, d['薯条'][::-1], label='薯条')
    plt.plot(labels, d['可乐'][::-1],  label='可乐')
    plt.legend()
    plt.show()
# 清空销售记录
def delete():
    with open('record.csv','w',encoding='utf8') as f:
        pass
    tk.messagebox.showinfo(message='清除记录成功！')
# 订餐函数
def menu():
    # 订餐提交函数
    def post():
        try:
            if e1.get() == '':
                n1 = 0
            else:
                n1 = int(e1.get())
            if e2.get() == '':
                n2 = 0
            else:
                n2 = int(e2.get())
            if e3.get() == '':
                n3 = 0
            else:
                n3 = int(e3.get())
            if e4.get() == '':
                n4 = 0
            else:
                n4 = int(e4.get())
            m = n1*10+n2*10+n3*5+n4*5
            text = f"""
        总共购买：
        双层牛肉堡：{n1}份
        单层鳕鱼堡：{n2}份
        薯条：{n3}份
        可乐：{n4}份
        总计：{m}元
        购买成功！
        """
            with open('record.csv','a+',encoding='utf8',newline='') as f:
                f.write(f'双层牛肉堡,{n1},{get_now_time()}\n')
                f.write(f'单层鳕鱼堡,{n2},{get_now_time()}\n')
                f.write(f'薯条,{n3},{get_now_time()}\n')
                f.write(f'可乐,{n4},{get_now_time()}\n')
            tk.messagebox.showinfo(message=text)
        except:
            tk.messagebox.showwarning(message='请输入正确的商品数量！')
    win2 = Toplevel(win1)
    win2.title('菜单')
    win2.geometry("450x800")
    photo1 = PhotoImage(file="1.png")
    lb1 = Label(win2,image=photo1)
    lb1.place(x=50, y=70,width = 150,height=170)
    Label(win2,text='双层牛肉煲（10元）').place(x=70,y=250)
    photo2 = PhotoImage(file="2.png")
    lb2 = Label(win2,image=photo2)
    lb2.place(x=260, y=70,width = 150,height=170)
    Label(win2,text='单层鳕鱼煲（10元）').place(x=280,y=250)
    photo3 = PhotoImage(file="3.png")
    lb3 = Label(win2,image=photo3)
    lb3.place(x=50, y=300,width = 150,height=170)
    Label(win2,text='薯条（5元）').place(x=90,y=480)
    photo4 = PhotoImage(file="4.png")
    lb4 = Label(win2,image=photo4)
    lb4.place(x=260, y=300,width = 150,height=170)
    Label(win2,text='可乐（5元）').place(x=300,y=480)
    Label(win2,text='请输入要购买的商品数量').place(x=150,y=530)
    Label(win2,text='双层牛肉煲:').place(x=50,y=580)
    e1 = Entry(win2)
    e1.place(x=150,y=580)
    Label(win2,text='双层牛肉煲:').place(x=50,y=610)
    e2 = Entry(win2)
    e2.place(x=150,y=610)
    Label(win2,text='薯条:').place(x=50,y=640)
    e3 = Entry(win2)
    e3.place(x=150,y=640)
    Label(win2,text='可乐:').place(x=50,y=670)
    e4 = Entry(win2)
    e4.place(x=150,y=670)
    Button(win2,text='提交',command=post).place(x=200,y=700)
    win2.mainloop()
# 主页面
win1 = Tk()
win1.title('点餐系统')
win1.geometry("600x450")
photo = PhotoImage(file='0.png')
Label(win1,image=photo).place(x=3,y=0,width=600,height=370)
# 为不同按钮绑定不同函数
Button(win1,text='点餐',command=menu).place(x=10,y=390,width=90,height=40)
Button(win1,text='总销量统计',command=count_all).place(x=105,y=390,width=90,height=40)
Button(win1,text='近7天销量统计(柱状图)',command=count_bar).place(x=200,y=390,width=140,height=40)
Button(win1,text='近7天销量统计(折线图)',command=count_line).place(x=345,y=390,width=140,height=40)
Button(win1,text='清空销售明细',command=delete).place(x=490,y=390,width=90,height=40)
win1.mainloop()
