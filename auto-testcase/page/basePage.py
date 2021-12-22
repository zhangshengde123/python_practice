from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):
    def __init__(self):
        try:
            self.driver = webdriver.Chrome()
            self.driver.implicitly_wait(2)
        except Exception:
            raise NameError("no such chrome")

    def open(self, url):
        if url != "":
            self.driver.maximize_window()
            self.driver.get(url)
        else:
            raise ValueError("请输入url地址")


    def find_element(self,*loc):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            print("%s 页面未找到 %s 元素" %(self, loc))

    def script(self, src):
        self.driver.execute_script(src)

    def send_keys(self, loc, value, clear_first = True, click_first = True):
        try:
            loc = getattr(self, "_%s" % loc)
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
        except AttributeError:
            print("%s 页面未找到 %s 元素" %(self, loc))


    # def allege(self, loc, value):
    #     try:
    #         loc = getattr(self, "_%s" % loc)
    #         text = self.find_element(*loc)
    #         self.ass


    def quit(self):
        self.driver.quit()
"""
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC


class BasePage(object):
    def __init__(self):
        try:
            self.driver = webdriver.Chrome()
        except Exception:
            raise NameError("not Chrome")

    def open(self, url):
        if url != "":
            self.driver.get(url)
            self.driver.maximize_window()
        else:
            raise ValueError("Please input a url")

    def find_element(self, *loc): #*loc任意数量是位置参数
        try:
            WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            print("%s 页面元素未找到 %s 元素" %(self, loc))

    def script(self, src):
        self.driver.execute_script(src)

    def send_keys(self, loc, value, clear_first = True, click_first = True):
        try:
            loc = getattr(self, "%s" %loc)
            if click_first:
                self.find_element(*loc).click()
            if clear_first:
                self.find_element(*loc).clear()
                self.find_element(*loc).send_keys(value)
        except AttributeError:
            print("%s 页面未找到 %s 元素" %(self, loc))

    def quit(self):
        self.driver.quit()

"""



"""
 def refresh(self):
        self.driver.refresh()
        time.sleep(1)

    def find_element(self, element_info):
        locator_type_name = element_info["定位方式"]
        locator_value_info = element_info["locator_value"]
        locator_timeout = element_info["timeout"]
        if locator_type_name == 'id':
            locator_type = By.ID
        elif locator_type_name == 'name':
            locator_type = By.NAME
        elif locator_type_name == 'className':
            locator_type = By.CLASS_NAME
        elif locator_type_name == 'xpath':
            locator_type = By.XPATH

        try:
            element = WebDriverWait(self.driver, locator_timeout).until(EC.invisibility_of_element_located(locator_value_info))
            return element
        except:
            print(f"{self}page find {locator_value_info} failure")


    def send_keys(self,element_info, value, first_clear = True):

        if first_clear:
            element = self.find_element(element_info)
            element.clear()
            element.send_keys(value)
        else:
            element = self.find_element(element_info)
            element.send_keys(value)


    def click(self, loc):
        self.driver.find_element(*loc).click()

"""