import re
import math
# 定义检查按钮函数
def check():
    global e_list
    e_list = []
    # 忽略一些计算函数
    flag = ['sin', 'sqr', 'abs']
    st = e.get()
    for i in flag:
        st = st.replace(i, '')
    d = []
    # 判断剩下的内容中有无字母变量
    for i in st:
        if i.isalpha() and i not in d:
            # 将字母变量存入d中
            d.append(i)
    # 将所有字母变量展示在界面上，让用户输入
    for i in d:
        Label(root, text=f'{i}:').pack()
        e0 = Entry(root)
        e0.pack()
        e_list.append([i,e0])
# 定义特定计算函数的处理
def d_replace(s):
    # 无限循环，直到找不到sin为止，将sin括号内的数值提取出来计算，然后再替换sin表达式
    while True:
        try:
            k = re.search('sin\((.*?)\)',s)
            r = s[k.span()[0]:k.span()[1]]
            res = r.replace('sin(','').replace(')','')
            res = eval(res)
            res = math.sin(res)
            res = str(round(res,2))
            s = s.replace(r, res)
        except:
            break
    # 下面的绝对值和开方同理
    while True:
        try:
            k = re.search('abs\((.*?)\)', s)
            r = s[k.span()[0]:k.span()[1]]
            res = r.replace('abs(', '').replace(')', '')
            res = eval(res)
            res = abs(res)
            res = str(round(res, 2))
            s = s.replace(r, res)
        except:
            break

    while True:
        try:
            k = re.search('sqr\((.*?)\)', s)
            r = s[k.span()[0]:k.span()[1]]
            res = r.replace('sqr(', '').replace(')', '')
            res = eval(res)
            res = math.sqrt(res)
            res = str(round(res, 2))
            s = s.replace(r, res)
        except:
            break

    return s
# 用用户输入的变量替换xy等未知量
def v_replace(s):
    for i in e_list:
        s = s.replace(i[0],i[1].get())
    return s
# 将中缀表达式替换为后缀表达式，并且计算结果
def convert(s):
    op_dict = {'^': 4, '*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    s = s.replace('**', '^')
    aw = []
    res = []
    for i in s:
        if i in "+-*/^()":
            res.append(''.join(aw))
            res.append(i)
            aw = []
        else:
            aw.append(i)
    if aw:
        res.append(''.join(aw))
    res = [i for i in res if i]
    resf = []
    i = 0
    while i < len(res):
        if res[i] == '-':
            try:
                float(res[i-1])
            except:
                resf.append(res[i]+res[i+1])
                i += 2
                continue
        resf.append(res[i])
        i += 1
    res = resf[::]
    n_stack = []
    o_stack = []

    for i in res:
        try:
            n_stack.append(float(i))
        except:
            if i == '(':
                o_stack.append(i)
            elif i == ')':
                top = o_stack.pop()
                while top != '(':
                    op2 = n_stack.pop()
                    op1 = n_stack.pop()
                    n_stack.append(eval(f'{op1}{top}{op2}'.replace('^','**')))
                    top = o_stack.pop()
            elif i in '+-*/^':
                while o_stack and op_dict[o_stack[-1]] >= op_dict[i]:
                    top = o_stack.pop()
                    op2 = n_stack.pop()
                    op1 = n_stack.pop()
                    n_stack.append(eval(f'{op1}{top}{op2}'.replace('^','**')))
                o_stack.append(i)
    while o_stack:
        top = o_stack.pop()
        op2 = n_stack.pop()
        op1 = n_stack.pop()
        n_stack.append(eval(f'{op1}{top}{op2}'.replace('^','**')))
    return n_stack[0]
# 定义计算按钮按下时两种可能的情况
def function():
    # 若可以顺利算出结果，则弹出结果
    try:
        d = v_replace(e.get())
        s = d_replace(d)
        res = convert(s)
        tk.messagebox.showinfo(title='结果', message=f'计算结果为：{round(res,2)}')
    # 否则就提示算式有误
    except:
        tk.messagebox.showinfo(title='结果', message=f'表达式或参数输入有误！')
import tkinter.messagebox
import tkinter as tk
from tkinter import *
root = Tk()
root.geometry('400x320')
Label(root,text='请输入计算表达式：').pack()
e = Entry(root,width=35)
e.pack()
Button(root,text='检查',command=check).place(x=150,y=250)
Button(root,text='计算',command=function).place(x=200,y=250)
root.mainloop()