import sys
sys.path.append("..")

import unittest
from time import sleep
from selenium import webdriver
import os
from loginPage import LoginPage


class TestRun(unittest.TestCase):
    def Setup(self):
        self.url = "http://dev-kaop-welfare.sdyxmall.com"
        sleep(2)
        self.content1 = "kaWelfare1"
        self.content2 = "kaWelfare1123"
        self.content3 = "k123456"
        self.PlatformLogin = LoginPage()

    def test_login(self):
        self.PlatformLogin = LoginPage()
        self.PlatformLogin.open("http://dev-kaop-welfare.sdyxmall.com")
        self.PlatformLogin.username_content("kaWelfare1")
        self.PlatformLogin.password_content("kaWelfare1123")
        self.PlatformLogin.verification_content("123456")
        self.PlatformLogin.click_btn()

        # self.assertEqual(self.find_element_by_xpath("//[@id='aside']/div/div"), '福利管理平台')
        # sleep(5)

    def TearDown(self):
        self.PlatformLogin.quit()


if __name__ == "__main__":
    unittest.main()

























