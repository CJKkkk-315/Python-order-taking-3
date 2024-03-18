import math
import tkinter.messagebox
import tkinter as tk
from tkinter import *
def funciton():
    filename = e1.get()
    res = ''
    with open(filename,'r',encoding='utf8') as f:
        data = ''.join(f.readlines())
    for ch in data:
        if '\u4e00' <= ch <= '\u9fff':
            res += ch
    e2.delete(0,END)
    e2.insert(0,len(res))
def clean():
    e1.delete(0,END)
    e2.delete(0,END)
root = Tk()
root.title("文本分析交互界面")
root.geometry('450x300')
Label(root,text='导入文件：').place(x=100,y=100)
e1 = Entry(root)
e1.place(x=170,y=100)
Label(root,text='字数统计：').place(x=100,y=150)
e2 = Entry(root)
e2.place(x=170,y=150)
Button(root,text='开始',command=funciton).place(x=130,y=200)
Button(root,text='清空',command=clean).place(x=250,y=200)
root.mainloop()