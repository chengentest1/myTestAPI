'''
1,从配置文件中读取stmp配置
2，从report文件夹下打开report.html,发送邮件
'''
import os
import smtplib
from email.mime.text import MIMEText



def send_email(report_file):

    with open(report_file,'rb') as f:
        body=f.read()
    #格式化email正文
    msg = MIMEText(body, "html", "utf-8")
    #配置email
    msg["Subject"] = 'Api Test Ressult'
    msg["From"] = 'chen_test_api@sina.com'
    msg["To"] = 'm18311135605@163,com'
    # 连接smtp服务器，发送邮件
    smtp = smtplib.SMTP()
    smtp.connect("smtp.sina.com")
    smtp.login('chen_test_api@sina.com', 'chengen123')
    smtp.sendmail('chen_test_api@sina.com', 'chengen_cg123@126.com', msg.as_string())
    print('邮件发送成功')
if __name__=="__main__":
    send_email('report.html')

