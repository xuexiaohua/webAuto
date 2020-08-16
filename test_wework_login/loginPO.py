#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from test_wework_login.registerPO import RegisterPO


class LoginPO:
    """
    登录页的po
    """
    def __init__(self, driver:WebDriver):
        self.driver = driver

    def scan(self):
        """
        扫描二维码
        :return:
        """
        pass

    def goto_register(self):
        """
        点击企业注册
        进入到企业注册的po
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR,".login_registerBar_link").click()
        return RegisterPO(self.driver)
