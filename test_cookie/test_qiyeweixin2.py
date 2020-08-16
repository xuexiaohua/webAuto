#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shelve
import time

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By

class TestQiYeWeixin2():
    def setup_method(self):
        coptions = Options()
        # 根据浏览器打开的调试端口进行通信
        # 命令窗口启动：浏览器要使用chrome.exe --remote-debugging-port=9222 开启调试
        coptions.debugger_address = "127.0.0.1:9222"
        self.driver = webdriver.Chrome()

    def test_work2(self):
        self.driver.get("https://work.weixin.qq.com/")
        # 创建或打开一个本地数据库
        db = shelve.open("cookies")
        # 取出本地数据库数据
        cookies = db["cookies"]
        for cookie in cookies:
            if "expiry" in cookie.keys():
                cookie.pop("expiry")
            self.driver.add_cookie(cookie)
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame#index")
        db.close()


