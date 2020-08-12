#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

from base import Base
from selenium import webdriver
from selenium.webdriver.support import expected_conditions


class TestLogin(Base):
    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    # def teardown(self):
    #     self.driver.quit()

    def test_login(self):
        self.driver.get("http://test-hx.ke.com")
        expected_conditions.invisibility_of_element(self.driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div[1]/div/div/div[2]/button"))
        knows_button = self.driver.find_element_by_xpath("/html/body/div[5]/div/div[2]/div/div[1]/div/div/div[2]/button")
        knows_button.click()
        expected_conditions.invisibility_of_element(self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[2]/div[1]/ul/li[2]/a"))
        login_link = self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[1]/div[2]/div/div[2]/div[1]/ul/li[2]/a")
        time.sleep(2)
        login_link.click()
        time.sleep(2)
        expected_conditions.invisibility_of_element(self.driver.find_element_by_xpath("//*[@id='username']"))
        user_name = self.driver.find_element_by_xpath("//*[@id='username']")
        expected_conditions.invisibility_of_element(self.driver.find_element_by_xpath("//*[@id='password']"))
        password = self.driver.find_element_by_xpath("//*[@id='password']")
        expected_conditions.invisibility_of_element(self.driver.find_element_by_xpath("//*[@id='login']/div[1]/div[2]/div/div[2]/div[2]/form/button"))
        login_button = self.driver.find_element_by_xpath("//*[@id='login']/div[1]/div[2]/div/div[2]/div[2]/form/button")
        user_name.send_keys(26028529)
        password.send_keys("H0meL1nk")
        login_button.click()

    # 创建任务
    def test_task_list(self):
        expected_conditions.invisibility_of_element(self.driver.find_element_by_xpath("//*[@id='root']/section/aside/div/div/ul/li[2]/a"))
        task_link = self.driver.find_element_by_xpath("//*[@id='root']/section/aside/div/div/ul/li[2]/a")
        task_link.click()
        expected_conditions.invisibility_of_element(self.driver.find_element_by_xpath("//*[@id='root']/section/section/div/div/span/span[1]/a"))
        task_title = self.driver.find_element_by_xpath("//*[@id='root']/section/section/div/div/span/span[1]/a")
        assert task_title == "任务管理"
        expected_conditions.invisibility_of_element(self.driver.find_element_by_xpath("//*[@id='root']/section/section/main/div/div/div[1]/div[1]/p"))
        search_task_title = self.driver.find_element_by_xpath("//*[@id='root']/section/section/main/div/div/div[1]/div[1]/p")
        assert search_task_title == "筛选任务"
        expected_conditions.invisibility_of_element(self.driver.find_element_by_xpath("//*[@id='root']/section/section/main/div/div/div[1]/div[2]/div[1]/span"))






