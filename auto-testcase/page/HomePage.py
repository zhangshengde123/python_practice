from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
from basePage import BasePage

class HomePage(BasePage):
    # 定位元素

    title_loc = (By.XPATH, "//[@id='aside']/div/div")



