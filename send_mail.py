from smtplib import *
from email.mime.multipart import MIMEMultipart
import email.mime.message


def send_mail(user,password):
    smtp_ssl = SMTP_SSL("smtp.163.com", 465)
    smtp_ssl.login(user, password)
    msg = MIMEMultipart()
    msg['From'] = "ZW282615SC@163.com"
    msg['To'] = "1097503158@qq.com"
    msg['Subject'] = "Hello world"
    smtp_ssl.send_message(msg, "ZW282615SC@163.com", ["1097503158@qq.com"])


if __name__ == '__main__':
    send_mail("ZW282615SC@163.com", "2b172b")