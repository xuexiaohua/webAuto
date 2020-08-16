#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class RegisterPO:
    """
    注册的po
    """
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def register(self):
        """
        输入内容
        点击下拉框
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR,"#corp_name").send_keys("霍格沃兹测试学院")
        self.driver.find_element(By.CSS_SELECTOR,"#manager_name").send_keys("MrXue")
        return True
