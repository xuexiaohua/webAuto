#!/usr/bin/env python
# -*- coding: utf-8 -*-
from time import sleep

from selenium.webdriver.support import expected_conditions

from base import Base

class TestFileUpload(Base):
    def test_fileUpload(self):
        self.driver.get("https://image.baidu.com")
        expected_conditions.invisibility_of_element(self.driver.find_element_by_xpath("//*[@id='sttb']/img[1]"))
        photo_button = self.driver.find_element_by_xpath("//*[@id='sttb']/img[1]")
        photo_button.click()
        self.driver.find_element_by_id("stfile").send_keys("D:\\workspace\\pycharmProjects\\webAuto\\screenshot\\test.png")
        sleep(2)

