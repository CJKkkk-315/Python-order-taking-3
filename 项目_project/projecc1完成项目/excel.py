import xlwings
import sys
import time
import os
from openpyxl  import  Workbook
def excel_copy(excelsrc,elcelsheet,excellocal,copylistA):
    ###  -----excelsrc = excel路径
    ###  -----excelsheet = excel的sheet名字
    ### ------copylistA = 嵌套列表 例如 [['a','b'],['1','2'],['3','4']]
    ###  -----  excellocal = excel的工作从哪里开始写入
    tarsrc = os.path.dirname(excelsrc)
    if os.path.exists(tarsrc):
        print('存在路径'+tarsrc)
        if os.path.exists(excelsrc):
            print('存在excel无需创建')
        else:
            W1 = Workbook()
            W1.save(excelsrc)
    else:
        os.makedirs(tarsrc)
        W1 = Workbook()
        W1.save(excelsrc)
        print('创建路径'+excelsrc)


    try :
        print(excelsrc)
        wb = xlwings.Book(excelsrc)
        print(1)
        ws = wb.sheets(elcelsheet)
        ws.range(excellocal).value = copylistA
        time.sleep(2)
        wb.save()
        print('已经完成')
    except Exception  as excelerror:
        print('失败'+str(excelerror)+'-----'+excelsrc)
        pass



