#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shelve
import time

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestQiYeWeixin():
    def setup_method(self):
        coptions = Options()
        # 根据浏览器打开的调试端口进行通信
        # 命令窗口启动：浏览器要使用chrome.exe --remote-debugging-port=9222 开启调试
        coptions.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome(options=coptions)

    # def teardown_method(self):
    #     self.driver.quit()

    # def test_baidu(self):
    #     self.driver.get("https://www.baidu.com")
    #     self.driver.find_element(By.ID,"kw").send_keys("霍格沃兹测试学院")
    #     self.driver.find_element(By.ID,"su").click()
    #     time.sleep(2)
    #     self.driver.find_element(By.LINK_TEXT,"霍格沃兹测试学院 – 测试开发工程师的黄埔军校").click()

    def test_wework(self):
        self.driver.find_element(By.ID, "menu_contacts").click()
        cookies = self.driver.get_cookies()
        print(cookies)
        # 创建/打开本地数据库
        db = shelve.open("cookies")
        # 将数据存放到本地数据库
        db["cookies"] = cookies
        db.close()


