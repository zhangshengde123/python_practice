import os
import smtplib
import time
from email import encoders
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header


def sendReport(file_path):
    sendfile = open(file_path,"rb").read()


    mail_host = 'smtp.qq.com'    #服务器地址
    mail_user = '3289643714@qq.com'  #发件人
    mail_pwd = 'dhbikizclxyochai'     #16位的授权码
    sender = '3289643714@qq.com'
    receivers = ['vundo@maizuo.com']


    msg = MIMEMultipart()
    msg['From'] = Header("测试组","utf-8")
    msg['To'] = Header("测试组", "utf-8")

    subject = '测试报告邮件'
    msg['Subject'] = Header(subject, 'utf-8')

    # 邮件正文内容
    msg.attach(MIMEText('自动化测试报告邮件发送测试……', 'plain', 'utf-8'))
    att1 = MIMEText(sendfile, "base64", "utf-8")
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att1["Content-Disposition"] = 'attachment; filename="report.html"'
    msg.attach(att1)
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pwd)
        smtpObj.sendmail(sender, receivers, msg.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")

def newReport(testReport):
        lists = os.listdir(testReport)  # 返回测试报告所在目录下的所有文件夹
        lists2 = sorted(lists)  # 获得升序排列后端测试报告列表
        # 获得最新一条测试报告的地址
        file_new = os.path.join(testReport, lists2[-1])
        print(file_new)
        return file_new

# ********************************
# 以下部分为测试代码，框架设计完毕真正运行时需注释掉
# ********************************
if __name__ == '__main__':
    test_report = r"E:\Program Files\web自动化测试用例\auto-testcase\report"                         #测试报告所在目录
    new_report = newReport(test_report)       #获取最新的测试报告
    print(new_report)
    sendReport(new_report)                           #发送测试报告邮件report.html









"""
def send_mail(subject):
    email_server = 'smtp.qq.com'    #服务器地址
    sender = '3289643714@qq.com'  #发件人
    password = 'dhbikizclxyochai'     #16位的授权码
    receiver = ['vundo@hyx.com']
    msg = MIMEMultipart()
    msg['Subject'] = subject   #邮件标题
    msg['From'] = '3289643714@qq.com<3289643714@qq.com>'
    msg['To'] = ";".join(receiver) #收件人
    # 正文中的图片，通过HTML格式放置图片
    mail_msg = '<p><img src="cid:image1"></p>'
    msg.attach(MIMEText(mail_msg, 'html', 'utf-8'))
    # 指定图片的存放路径


    fp = open(r'E:\Program Files\web自动化测试用例\auto-testcase\snapshot\redriver.jpg', 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()
    # 定义图片id，从而在HTML文本中引用
    msgImage.add_header('Content-ID', '<image1>')
    msg.attach(msgImage)

    conttype = 'application/octet-stream'
    maintype, subtype = conttype.split('/', 1)
    #附件中的图片
    image=MIMEImage(open(r'E:\Program Files\web自动化测试用例\auto-testcase\snapshot\redriver.jpg','rb').read(), _subtype=subtype)
    image.add_header('Content-Disposition', 'attachment', filename='redriver.jpg')
    msg.attach(image)
    #附件中由HTMLTestRunner生成的测试报告
    file = MIMEBase(maintype, subtype)
    file.set_payload(open(r'E:\Program Files\web自动化测试用例\auto-testcase\report\20211009155724_login_Ressult.html',
'rb').read())
    file.add_header('Content-Disposition','attachment',filename='自动化测试报告.html')
    encoders.encode_base64(file)
    msg.attach(file)

    #发送
    try:
        smtp = smtplib.SMTP()
        smtp.connect(email_server, 25)
        smtp.login(sender, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
        print('发送成功！')

    except:
        print('发送失败！')

if __name__ == '__main__':
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    subject = '自动化测试报告(' + now + ')'
    send_mail(subject)
"""