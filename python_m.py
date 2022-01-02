import yagmail
yagmail.register("13406396981@139.com","zxf19751208")
yag = yagmail.SMTP( user="13406396981@139.com", host='smtp.139.com')
contents = [
'这是第一段正文内容',
'这是第二段正文内容',
yagmail.inline('e:\\zhang\\favicon.ico'),
'<a href="https://www.baidu.com">百度网站</a>',
'e:\\zhang\\nmap.lst']
yag.send("13406396981@139.com","测试",contents)
#yag.send(
#    to=['13406396981@139.com'],
#    cc='willares@163.com',
#    subject='学习发送邮件1',
#    contents='你好，你今天开心吗？')
  #  attachments=[r'd://log.txt', r'd://baidu_img.jpg'])
yag.close()
