from Comm.MsSql import MSSQL
import xlrd
def writesql():
    msql = MSSQL('.','sa','mrsoft','sihuo')  #sql连接
    table = '[sihuo].[dbo].[cuoti]'###数据库对象
    src_excel = r'C:\Users\2\Desktop\111.xlsx'  #路径 excel
    df = xlrd.open_workbook(src_excel)
    df1 = df.sheets()[0]
    for r in range(1,199):
        ulrr = df1.cell(r, 0).value
        title = df1.cell(r, 1).value
        answer = df1.cell(r, 2).value
        answer_true = df1.cell(r, 3).value
        answer_txt = df1.cell(r, 4).value
        region = df1.cell(r, 5).value

        insert = "insert into "+table+"([url],[col1],[col2],[col3],[col4],col5)  VALUES (%s,%s,%s,%s,%s,%s) "
        msql.ExecNonQuery(insert,(ulrr,title,answer,answer_true,answer_txt,region))
        print('插入成功第%s条数据'%r)

        print(region)
writesql()

