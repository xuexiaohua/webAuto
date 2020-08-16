#!/usr/bin/env python
# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class BasePage:
    _driver = None
    _base_url = ""

    def __init__(self, is_reuser=False):
        if not is_reuser:
            chrome_options = Options()
            chrome_options.debugger_address = "127.0.0.1:9222"
            self._driver = webdriver.Chrome(options=chrome_options)
            self._driver.implicitly_wait(3)
        if self._base_url != "":
            self._driver.get(self._base_url)

    """
    封装find_element方法
    """
    def find(self, by, locator):
        return self._driver.find_element(by, locator)
