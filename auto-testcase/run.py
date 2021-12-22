import unittest
import time
from HTMLTestRunner import HTMLTestRunner
from utils.send_mail import send_mail

if __name__ =='__main__':
    testcases_dir = './TestCase/'
    testreport = './report/'
suite = unittest.defaultTestLoader.discover(testcases_dir,pattern='login.py')
filename = testreport + time.strftime("%Y%m%d%H%M%S") + "_login_" + "Ressult.html"
fp = open(filename, "wb")
runner = HTMLTestRunner(stream=fp, title="福利平台登录测试报告", description="测试环境")
runner.run(suite)
fp.close()
now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
subject = '自动化测试报告(' + now + ')'
send_mail(subject)