#!/usr/bin/env python
# -*- coding: utf-8 -*-
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

from test_wework_login.loginPO import LoginPO
from test_wework_login.registerPO import RegisterPO


class IndexPO:
    """
    登录页PO
    """
    def __init__(self):
        chrome_options = Options()
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get("https://work.weixin.qq.com/")

    def goto_register(self):
        """
        点击立即注册
        进入到立即注册的po
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR,".index_head_info_pCDownloadBtn").click()
        return RegisterPO(self.driver)

    def goto_login(self):
        """
        点击企业登录
        进入到企业登录的po
        :return:
        """
        self.driver.find_element(By.CSS_SELECTOR,".index_top_operation_loginBtn").click()
        return LoginPO(self.driver)