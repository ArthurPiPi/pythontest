import time
import schedule
import yagmail
import datetime
def morning():
    content=["定时发送测试",'定时发送时间测试']
    yag=yagmail.SMTP(user='13406396981@139.com',password='zxf19751208',host='SMTP.139.com')
    yag.send("13406396981@139.com","测试邮件",content)
schedule.every().day.at('17:05').do(morning)
while True:
    schedule.run_pending()
    time.sleep(1)