import tkinter
import 谜语系统 as st#这个是我用来返回初始界面的
def daojishi(root,tim):
    def foo():
        global timm
        clock = time_lable.after(1000, foo)  # 延迟调用foo，每1000毫秒一次
        timm = timm - 1  # 倒计时
        if timm == 0:  # 如果倒计时为零时
            root.destroy()#销毁我们的显示界面
            st.main()#放回初始界面
        else:
            time_lable['text'] = str(timm)  # 设置按钮显示文字倒计时
    global timm
    timm=tim
    time_lable = tkinter.Label(root, text=str(timm), font=('Arial', 48),bg='white')
    time_lable.place(relx=0.01, rely=0.2)
    time_lable.after(1000, foo)  # 每1000毫秒调用一次foo
