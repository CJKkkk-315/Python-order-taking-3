import os
import matplotlib.pyplot as plt
import matplotlib
from tkinter import *
import tkinter as tk
import tkinter.messagebox
matplotlib.use('TkAgg')
plt.rcParams['font.sans-serif'] = ['SimHei']
filelist = [file for file in os.listdir() if file.split('.')[1] == 'csv']
filelist.sort()
mouths_data = []
for file in filelist:
    d = {}
    data = [i.replace('\n', '').split(',') for i in open(file, encoding='utf8').readlines() if any(i.replace('\n', '').split(','))][1:]
    if not mouths_data:
        for item in data:
            if item[0] not in d:
                d[item[0]] = {}
            d[item[0]][item[1]] = list(map(float,item[2:]))
    else:
        for item in data:
            if item[0] not in d:
                d[item[0]] = {}
            number = int(item[-1]) - mouths_data[-1][item[0]][item[1]][-1]
            d[item[0]][item[1]] = list(map(float,item[2:-1]+[number]))
    mouths_data.append(d)
def draw1():
    labels = []
    for i in range(len(mouths_data)):
        labels.append(str(i+1)+'月')
    for key in mouths_data[0]:
        value = []
        for i in range(len(mouths_data)):
            value.append(sum([j[1]*j[2] for j in mouths_data[i][key].values()]))
        plt.plot(labels, value, label=key)
    plt.title('销售额')
    plt.legend()
    plt.show()
def draw2():
    labels = []
    for i in range(len(mouths_data)):
        labels.append(str(i+1)+'月')
    for key in mouths_data[0]:
        value = []
        for i in range(len(mouths_data)):
            value.append(sum([j[2] for j in mouths_data[i][key].values()]))
        plt.plot(labels, value, label=key)
    plt.title('销售数量')
    plt.legend()
    plt.show()
def draw3():
    labels = []
    for i in range(len(mouths_data)):
        labels.append(str(i+1)+'月')
    for key in mouths_data[0]:
        value = []
        for i in range(len(mouths_data)):
            value.append(sum([(j[1]-j[0])*j[2] for j in mouths_data[i][key].values()]))
        plt.plot(labels, value, label=key)
    plt.title('销售利润')
    plt.legend()
    plt.show()
def all_sell():
    m1 = 0
    m2 = 0
    data = [i.replace('\n', '').split(',') for i in open(filelist[-1], encoding='utf8').readlines() if any(i.replace('\n', '').split(','))][1:]
    for item in data:
        m1 += float(item[3])*int(item[4])
        m2 += (float(item[3])-float(item[2]))*int(item[4])
    tk.messagebox.showinfo(message=f'总销售额为：{m1}\n总利润为：{m2}')
def save():
    t = [i.replace('\n', '').split(',') for i in open(filelist[-1], encoding='utf8').readlines() if any(i.replace('\n', '').split(','))][1:]
    t.sort(key=lambda x:x[-1])
    t = t[:10]
    with open('特价书籍.csv','w',encoding='utf8',newline='') as f:
        for i in t:
            i[3] = str(round(0.9*float(i[3]),2))
            f.write(','.join(i)+'\n')
    tk.messagebox.showinfo(message=f'保存成功！')
win1 = Tk()
win1.title('销量可视化')
win1.geometry("300x350")
Label(win1).pack()
Button(win1,text='累计销售额和利润',command=all_sell).pack()
Label(win1).pack()
Button(win1,text='分类销售额可视化',command=draw1).pack()
Label(win1).pack()
Button(win1,text='分类销售数量可视化',command=draw2).pack()
Label(win1).pack()
Button(win1,text='分类销售利润可视化',command=draw3).pack()
Label(win1).pack()
Button(win1,text='特价书籍保存',command=save).pack()
win1.mainloop()
