import pymysql
# 导入pymysql模块
import pymysql
# 连接database
conn = pymysql.connect(
    host='localhost',
user ='', password = '',
database ='',
charset ='utf8')
# 得到一个可以执行SQL语句的光标对象
cursor = conn.cursor()  # 执行完毕返回的结果集默认以元组显示
# 定义要执行的SQL语句
sql = """
select Test_result from test
"""
cursor.execute(sql)
result = cursor.fetchall()
data = []
for item in result:
    data.append(item[0])
print(data)
# 关闭光标对象
cursor.close()
# 关闭数据库连接
conn.close()
p = 0
import re
for i in data:
    r = re.match('pass', i)
    if r != None:
        p += 1
res = p/len(data)
if res > 0.9:
    text = '1'
else:
    text = '2'
import smtplib
from email.mime.text import MIMEText
from email.header import Header
mail_host = "smtp.qq.com"
mail_user = "1121033787@qq.com"  # 发送邮箱
mail_pass = ""  # 密钥
sender = '1121033787@qq.com'  # 发送邮箱
receivers = ['1121033787@qq.com']  # 接受邮箱列表
message = MIMEText(text, 'plain', 'utf-8')
message['From'] = Header("发送方", 'utf-8')
message['To'] = Header("接收方", 'utf-8')
subject = '结果'
message['Subject'] = Header(subject, 'utf-8')
smtpObj = smtplib.SMTP()
smtpObj.connect(mail_host, 25)
smtpObj.login(mail_user, mail_pass)
smtpObj.sendmail(sender, receivers, message.as_string())
print("邮件发送成功")
