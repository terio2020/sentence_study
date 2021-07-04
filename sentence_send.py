# %%
import smtplib
from email.header import Header
from email.mime.text import MIMEText
import sentence_acq
import requests

def send_mails():
    
    all = sentence_acq.getContent()
    
    content_wechat = ("<h3>" + all[0] + "</h3>" + "<br>" +
          "<h5>" + all[1] + "</h5>" + "<br>" + "<h5>" +
          "<a href=\"" + all[2] + "\">点击查看" + "</h5>")

    # 这里使用Pushplus+来推送信息
    url = '{}'.format(content_wechat)
    reqp = requests.get(url)
    

if __name__ == '__main__':
    send_mails()