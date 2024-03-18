

import matplotlib.pyplot as plt
import matplotlib as mpl
import pandas as pd
from collections import Counter
from txt测试 import error_Grab
import tkinter.messagebox
import tkinter as tk
from tkinter import *
from PIL import Image,ImageTk
def get_image(filename,width,height):
    im = Image.open(filename).resize((width,height))
    return ImageTk.PhotoImage(im)

mpl.rcParams['font.sans-serif'] = ['STFangsong']
mpl.rcParams['font.serif'] = ['STFangsong']



data=pd.read_excel('111.xlsx')
Right=data['答案']
Answer=data['回答']
Subject=data['科目']

AnalyzeData=[]
for i in range(len(Right)):
    AnalyzeData.append((Subject[i].replace('高中','').replace('题库',''),Right[i],Answer[i]))

SW={}
for line in AnalyzeData:
    if line[1]!=line[2]:
        if not SW.get(line[0]):
            SW[line[0]]=0
        SW[line[0]]+=1
SX=[]
WN=[]
for k,v in SW.items():
    SX.append(k)
    WN.append(v)

#求一下错题率
STotal=Counter(Subject)
WPD={}
for k,v in SW.items():
    if STotal.get('高中'+k+'题库'):
        WPD[k]=v/STotal['高中'+k+'题库']
WP=[v for k,v in WPD.items()]

def draw1():
    plt.scatter(SX,WN,color='r')
    plt.plot(SX,WN)
    plt.title('高中各科错题具体数量')
    for x, y in zip(SX, WN):
        plt.text(x, y + 0.3, '%.0f' % y, ha='center', va='bottom', fontsize=10.5)
    plt.savefig('各科错题量.png')
    plt.show()

def draw2():
    plt.scatter(SX,WP,color='r')
    plt.plot(SX,WP)
    plt.title('高中各科错题率')
    for x, y in zip(SX, WP):
        plt.text(x, y + 0.003, '%.03f' % y, ha='center', va='bottom', fontsize=10.5)
    plt.savefig('各科错题率.png')
    plt.show()
def draw():
    root1 = Toplevel()
    root1.title("爬虫可视化")
    root1.geometry('800x600')
    can_root = Canvas(root1, width=800, height=600)
    can_root.create_image(400, 300, image=im_root)
    can_root.pack()
    Button(root1, text='错题量可视化', width=16, heigh=6, command=draw1).place(x=200, y=200)
    Button(root1, text='错题率可视化', width=16, heigh=6, command=draw2).place(x=500, y=200)
root = Tk()
root.title("爬虫可视化")
root.geometry('800x600')
can_root = Canvas(root,width=800,height=600)
im_root = get_image('back.jpg',800,600)
can_root.create_image(400,300,image=im_root)
can_root.pack()
Button(root,text='数据爬取',width=16,heigh=6,command=error_Grab).place(x=200,y=200)
Button(root,text='数据分析',width=16,heigh=6,command=draw).place(x=500,y=200)

root.mainloop()

