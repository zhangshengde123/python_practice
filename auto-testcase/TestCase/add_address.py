from selenium import webdriver
import time
import unittest

"""新增收货地址"""
class add_address(unittest.TestCase):
    # 1.打开浏览器
    def setUp(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(2)
        pass

    # # 测试后执行
    # def tearDown(self) -> None:
    #     self.driver.quit()
    #     pass

    #  添加cookies信息
    #  user_id = {'name': 'COOKIE_USER_ID', 'value': '1000090'}
    #  cookie_user_x_token = {'name': 'COOKIE_USER_X_TOKEN', 'value': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhZ2VudElkIjoiMzAwMCIsInRpbWVzdGFtcCI6MTYwOTM5ODQwMCwidXNlcklkIjoxMDAwMDkwfQ.P13vHuKgb6K2sb-5MN_BaPMPzvz2KMsnkMxp545zDF4'}
    def add_address_success(self):
        """添加地址成功的测试用例"""

        self.driver.get('http://dev-m.sdyxmall.com/')   # 通过驱动来执行指定的网页

        self.driver.add_cookie({'name': 'COOKIE_USER_ID', 'value': '1000090'})
        self.driver.add_cookie({'name': 'COOKIE_USER_X_TOKEN', 'value': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhZ2VudElkIjoiMzAwMCIsInRpbWVzdGFtcCI6MTYwOTM5ODQwMCwidXNlcklkIjoxMDAwMDkwfQ.P13vHuKgb6K2sb-5MN_BaPMPzvz2KMsnkMxp545zDF4'})

        #刷新页面
        self.driver.refresh()

        time.sleep(3)
        self.driver.find_element_by_xpath("//div[@class='close-btn']").click()


        # 跳转至地址列表页 //div[@class="common address"]
        self.driver.find_element_by_class_name("center").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@class='avatar']/img").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@class='common address']").click()
        time.sleep(2)
        # 跳转新增地址页面<div class="address-form ai-address-form"><textarea
        self.driver.find_element_by_xpath("//div[@class='address-list']/div/div[2]").click()
        time.sleep(1)
        recognition_frame = self.driver.find_element_by_xpath("//div[@class='address-form ai-address-form']/textarea")
        recognition_frame.send_keys("灰姑娘 156446465545 广东省深圳市宝安区宝安中心壹方城666号")
        time.sleep(1)
        self.driver.find_element_by_xpath("//div[@class='address-form ai-address-form']/div/div[1]").click()
        self.driver.find_element_by_class_name("btn-save").click()
        time.sleep(1)
        self.driver.find_element_by_xpath("//button[2]").click()
        time.sleep(3)

        """断言"""
        # /html/body/div[1]/div[2]
        address = self.driver.find_element_by_xpath("html//body/div[1]/div[2]/div/div[1]/div[2]/div/div").text
        self.assertIn("灰姑娘", address)

        # 测试后执行
    def tearDown(self) -> None:
        self.driver.quit()
        pass