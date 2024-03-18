TempStr=input("请输入带有符号的温度值:")
if TempStr[-1] == 'F':
    try:
        C=(eval(TempStr[0:-1])-32)/1.8
        K = C + 273.15
        print("转换后的摄氏度是{:.2f}C".format(C))
        print("转换后的开氏度是{:.2f}K".format(K))
    except:
        print("输入错误")
elif TempStr[-1] == 'C':
    try:
        F=1.8*eval(TempStr[0:-1])+32
        K = eval(TempStr[0:-1]) + 273.15
        print("转换后的华氏度是{:.2f}F".format(F))
        print("转换后的开氏度是{:.2f}K".format(K))
    except:
        print("输入错误")
elif TempStr[-1] == 'K':
    try:
        C=eval(TempStr[0:-1]) - 273.15
        F=1.8*C+32
        print("转换后的华氏度是{:.2f}F".format(F))
        print("转换后的摄氏度是{:.2f}K".format(C))
    except:
        print("输入错误")
else:
    print("输入错误")