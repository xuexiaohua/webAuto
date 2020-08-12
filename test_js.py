#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest

from base import Base
import time

class TestJS(Base):
    @pytest.mark.skip
    def test_js_scroll(self):
        self.driver.get("https://www.baidu.com")
        self.driver.find_element_by_id("kw").send_keys("selenium测试")
        element = self.driver.execute_script("return document.getElementById('su')")
        element.click()
        time.sleep(2)
        self.driver.execute_script("document.documentElement.scrollTop=10000")
        time.sleep(2)
        print(self.driver.execute_script("return document.title;return JSON.stringify(performance.timing)"))

    def test_datetime(self):
        self.driver.get("https://www.12306.cn/index/")
        time_element = self.driver.execute_script("a=document.getElementById('train_date');a.removeAttribute('readonly');"
                                                  "a.value='2020-12-30'")
        time.sleep(3)


