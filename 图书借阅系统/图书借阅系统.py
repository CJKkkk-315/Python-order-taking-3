from tkinter import *
import tkinter as tk
import tkinter.messagebox
from datetime import *
import time
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
def get_time():
    ts = time.time()
    ta = time.localtime(ts)
    t = time.strftime('%Y%m%d', ta)
    return t
with open('学生信息.txt',encoding='utf8') as f:
    userlist = [i.replace('\n','').split(',') for i in f.readlines()]
with open('图书信息.txt',encoding='utf8') as f:
    booklist = [i.replace('\n','').split(',') for i in f.readlines()]
with open('借阅信息.txt',encoding='utf8') as f:
    recordlist = [i.replace('\n','').split(',') for i in f.readlines()]
print(recordlist)
def f1():
    def insert():
        if e.get().split(' ')[0] in [i[0] for i in userlist]:
            tk.messagebox.showinfo(message='学号已存在！')
            return
        if len(e.get().split(' ')) != 4:
            tk.messagebox.showinfo(message='格式错误！')
            return
        userlist.append(e.get().split(' '))
        tk.messagebox.showinfo(message='插入成功')
    root2 = Toplevel(root1)
    root2.title('图书借阅系统')
    root2.geometry("600x600")
    Label(root2, text='请输入学生的以下信息，以空格分隔：').pack()
    Label(root2, text='学号 姓名 性别 班级').pack()
    e = Entry(root2,width=70)
    e.pack()
    Button(root2, text='提交', command=insert).pack()
def f2():
    def insert():
        if e.get().split(' ')[0] in [i[0] for i in booklist]:
            tk.messagebox.showinfo(message='书号已存在！')
            return
        if len(e.get().split(' ')) != 4:
            tk.messagebox.showinfo(message='格式错误！')
            return
        booklist.append(e.get().split(' '))
        tk.messagebox.showinfo(message='插入成功')
    root2 = Toplevel(root1)
    root2.title('图书借阅系统')
    root2.geometry("600x600")
    Label(root2, text='请输入图书的以下信息，以空格分隔：').pack()
    Label(root2, text='书号 书名 出版社 作者 价格 库存').pack()
    e = Entry(root2,width=70)
    e.pack()
    Button(root2, text='提交', command=insert).pack()
def f3():
    def insert():
        if e1.get() not in [i[0] for i in userlist] or e2.get() not in [i[0] for i in booklist]:
            tk.messagebox.showinfo(message='学号或书号不存在!')
            return
        if int([i for i in booklist if i[0] == e2.get()][0][-1]) == 0:
            tk.messagebox.showinfo(message='库存不足!')
            return
        if len([i[0] for i in recordlist if i[0] == e1.get() and not i[-1]]) == 5:
            tk.messagebox.showinfo(message='超出借阅次数!')
            return
        recordlist.append([e1.get(),e2.get(),get_time(),''])
        for i in range(len(booklist)):
            if booklist[i][0] == e2.get():
                booklist[i][-1] = str(int(booklist[i][-1])-1)
        tk.messagebox.showinfo(message='借阅成功!')
    root2 = Toplevel(root1)
    root2.title('图书借阅系统')
    root2.geometry("600x600")
    Label(root2, text='请输入借阅学生学号').pack()
    e1 = Entry(root2,width=70)
    e1.pack()
    Label(root2, text='请输入借阅图书书号').pack()
    e2 = Entry(root2, width=70)
    e2.pack()
    Button(root2, text='提交', command=insert).pack()
def f4():
    def insert():
        try:
            if [e1.get(),e2.get()] not in [[i[0],i[1]] for i in recordlist] or [i for i in recordlist if (i[0] == e1.get() and i[1] == e2.get() and not i[-1])][0][-1]:
                tk.messagebox.showinfo(message='没有该条借阅信息')
                return
        except:
            tk.messagebox.showinfo(message='没有该条借阅信息')
            return
        for i in range(len(recordlist)):
            if recordlist[i][0] == e1.get() and recordlist[i][1] == e2.get() and not recordlist[i][-1]:
                recordlist[i][-1] = get_time()
                break
        for i in range(len(booklist)):
            if booklist[i][0] == e2.get():
                booklist[i][-1] = str(int(booklist[i][-1])+1)
                break
        tk.messagebox.showinfo(message='归还成功!')
    root2 = Toplevel(root1)
    root2.title('图书借阅系统')
    root2.geometry("600x600")
    Label(root2, text='请输入归还学生学号').pack()
    e1 = Entry(root2, width=70)
    e1.pack()
    Label(root2, text='请输入归还图书书号').pack()
    e2 = Entry(root2, width=70)
    e2.pack()
    Button(root2, text='提交', command=insert).pack()
def f5():
    def insert():
        root3 = Toplevel(root2)
        root3.title('图书借阅系统')
        root3.geometry("600x600")
        Label(root3, text="{:^20s}{:^20s}{:^20s}{:^20s}".format(*['学生学号','图书书号','借阅日期','归还日期'])).pack()
        text = '\n'.join(["{:^20s}{:^20s}{:^20s}{:^20s}".format(*i) for i in recordlist if i[0] == e1.get()])
        Label(root3, text=text, justify='left' ).pack()
    root2 = Toplevel(root1)
    root2.title('图书借阅系统')
    root2.geometry("600x600")
    Label(root2, text='请输入查询学生学号').pack()
    e1 = Entry(root2, width=70)
    e1.pack()
    Button(root2, text='提交', command=insert).pack()
def f6():
    def insert():
        root3 = Toplevel(root2)
        root3.title('图书借阅系统')
        root3.geometry("600x600")
        Label(root3, text="{:^20s}{:^20s}{:^20s}{:^20s}".format(*['学生学号','图书书号','借阅日期','归还日期'])).pack()
        text = '\n'.join(["{:^20s}{:^20s}{:^20s}{:^20s}".format(*i) for i in recordlist if i[1] == e1.get()])
        Label(root3, text=text, justify='left' ).pack()
    root2 = Toplevel(root1)
    root2.title('图书借阅系统')
    root2.geometry("600x600")
    Label(root2, text='请输入查询图书书号').pack()
    e1 = Entry(root2, width=70)
    e1.pack()
    Button(root2, text='提交', command=insert).pack()
def f7():
    def insert():
        res = len([i for i in booklist if i[2] == e1.get()])
        tk.messagebox.showinfo(message=f'该出版社的图书藏书量为{res}本')
    root2 = Toplevel(root1)
    root2.title('图书借阅系统')
    root2.geometry("600x600")
    Label(root2, text='请输入查询的出版社名称').pack()
    e1 = Entry(root2, width=70)
    e1.pack()
    Button(root2, text='提交', command=insert).pack()
def f8():
    root2 = Toplevel(root1)
    root2.title('图书借阅系统')
    root2.geometry("600x600")
    res = []
    date1 = datetime.now()
    for i in recordlist:
        date2 = datetime.strptime(i[-2], "%Y%m%d")
        duration = date1 - date2
        day = duration.days
        if not i[-1] and day > 90:
            res.append(i)
    Label(root2, text="{:^20s}{:^20s}{:^20s}{:^20s}".format(*['学生学号', '图书书号', '借阅日期', '归还日期'])).pack()
    text = '\n'.join(["{:^20s}{:^20s}{:^20s}{:^20s}".format(*i) for i in res])
    Label(root2, text=text, justify='left').pack()
def f9():
    root2 = Toplevel(root1)
    root2.title('图书借阅系统')
    root2.geometry("600x600")
    name_index = {}
    count = {}
    for i in userlist:
        name_index[i[0]] = i[1]
    for i in recordlist:
        count[name_index[i[0]]] = count.get(name_index[i[0]],0) + 1
    rank = sorted(count.items(),key=lambda x:x[1],reverse=True)
    for i in rank:
        Label(root2, text=f"姓名：{i[0]}   借阅数量：{i[1]}").pack()
def f10():
    name_index = {}
    count = {}
    for i in userlist:
        name_index[i[0]] = i[1]
    for i in recordlist:
        count[name_index[i[0]]] = count.get(name_index[i[0]], 0) + 1
    rank = list(count.items())
    x = [i[0] for i in rank]
    y = [i[1] for i in rank]
    plt.plot(x,y)
    plt.show()

    count = {}
    for i in booklist:
        count[i[2]] = count.get(i[2], 0) + 1
    rank = list(count.items())
    x = [i[0] for i in rank]
    y = [i[1] for i in rank]
    plt.pie(labels=x, x=y)
    plt.show()
root1 = Tk()
root1.title('图书借阅系统')
root1.geometry("300x580")
Label(root1,text='').pack()
Button(root1, text='增加学生信息', command=f1,width=15).pack()
Label(root1,text='').pack()
Button(root1, text='增加图书信息', command=f2,width=15).pack()
Label(root1,text='').pack()
Button(root1, text='借阅图书', command=f3,width=15).pack()
Label(root1,text='').pack()
Button(root1, text='归还图书', command=f4,width=15).pack()
Label(root1,text='').pack()
Button(root1, text='查阅学生借阅信息', command=f5,width=15).pack()
Label(root1,text='').pack()
Button(root1, text='查阅图书借阅信息', command=f6,width=15).pack()
Label(root1,text='').pack()
Button(root1, text='查阅出版社信息', command=f7,width=15).pack()
Label(root1,text='').pack()
Button(root1, text='查阅逾期学生信息', command=f8,width=15).pack()
Label(root1,text='').pack()
Button(root1, text='统计学生借阅数量', command=f9,width=15).pack()
Label(root1,text='').pack()
Button(root1, text='数据可视化', command=f10,width=15).pack()
Label(root1,text='').pack()
root1.mainloop()
with open('学生信息.txt','w',encoding='utf8') as f:
    for i in userlist:
        f.write(','.join(i)+'\n')
with open('图书信息.txt','w',encoding='utf8') as f:
    for i in booklist:
        f.write(','.join(i)+'\n')
with open('借阅信息.txt','w',encoding='utf8') as f:
    for i in recordlist:
        f.write(','.join(i)+'\n')
