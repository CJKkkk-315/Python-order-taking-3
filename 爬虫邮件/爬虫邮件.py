import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time
def get_now_time():
    now =  time.localtime()
    now_time = time.strftime("%Y-%m-%d", now)
    return now_time
data = [
{'发布部门':'科技部门','发布时间':'2022-07-01','接受范围':'科技部门','有效期限':'30天','标题':'xxx的通知'},
{'发布部门':'非科技部门','发布时间':'2022-07-02','接受范围':'科技部门','有效期限':'30天','标题':'xxx的通知'},
{'发布部门':'科技部门','发布时间':'2022-07-02','接受范围':'科技部门','有效期限':'30天','标题':'xxx的通知'},
{'发布部门':'非科技部门','发布时间':'2022-07-05','接受范围':'科技部门','有效期限':'30天','标题':'xxx的通知'},
{'发布部门':'科技部门','发布时间':'2022-07-04','接受范围':'科技部门','有效期限':'30天','标题':'xxx的通知'},
{'发布部门':'非科技部门','发布时间':'2022-07-01','接受范围':'科技部门','有效期限':'30天','标题':'xxx的通知'},
{'发布部门':'科技部门','发布时间':'2022-07-05','接受范围':'科技部门','有效期限':'30天','标题':'xxx的通知'},
{'发布部门':'科技部门','发布时间':'2022-07-05','接受范围':'科技部门','有效期限':'30天','标题':'yyy的通知'}
 ]
content = ''
for item in data:
    if item['发布时间'] == get_now_time() and item['发布部门'] == '科技部门':
        content += f'发布时间：{item["发布时间"]}  接受范围：{item["接受范围"]}  有效期限：{item["有效期限"]}  标题：{item["标题"]} \n'
if content:
    mail_host = "smtp.qq.com"
    mail_user = ""  # 发送邮箱
    mail_pass = ""  # 密钥
    sender = ''  # 发送邮箱
    receivers = []  # 接受邮箱列表
    message = MIMEText(content, 'plain', 'utf-8')
    message['From'] = Header("发送方", 'utf-8')
    message['To'] = Header("接收方", 'utf-8')
    subject = '今日此网站新增信息'
    message['Subject'] = Header(subject, 'utf-8')
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("邮件发送成功")