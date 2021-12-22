from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
from basePage import BasePage

class LoginPage(BasePage):
    # 定位元素
    username_loc = (By.ID, "username")
    password_loc = (By.ID, "password")
    verification_loc = (By.ID, "verification")
    button_loc = (By.XPATH, "//button[contains(@type,'submit')]")
    assert_loc = (By.XPATH, "//div[text() = '福利管理平台']")

    def username_content(self, content1):
        usernameContent = self.find_element(*self.username_loc)
        usernameContent.send_keys(content1)

    def password_content(self, content2):
        passwordContent = self.find_element(*self.password_loc)
        passwordContent.send_keys(content2)

    def verification_content(self, content3):
        verificationContent = self.find_element(*self.verification_loc)
        verificationContent.send_keys(content3)

    def click_btn(self):
        clickBtn = self.find_element(*self.button_loc)
        clickBtn.click()


# if __name__ == '__main__':
#     PlatformLogin = LoginPage()
#     PlatformLogin.open_url("http://dev-kaop-welfare.sdyxmall.com")
#     PlatformLogin.username_content("kaWelfare1")
#     PlatformLogin.password_content("kaWelfare1123")
#     PlatformLogin.verification_content("123456")
#     PlatformLogin.click_btn()
#     PlatformLogin.quit()
