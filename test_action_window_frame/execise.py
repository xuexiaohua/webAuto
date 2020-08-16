#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver import ActionChains, TouchActions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestHogwards():
    def setup(self):
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown(self):
        # self.driver.quit()
        pass

    # def test_hogwards(self):
    #     self.driver.get("https://ceshiren.com")
    #     self.driver.find_element_by_link_text("热门").click()
    #     self.driver.save_screenshot("./screenshot/test.png")
    #     self.driver.find_element_by_link_text("接口重试功能如何测试").click()
    #     # time.sleep(1)
    #     WebDriverWait(self.driver, 10).until(self.driver.find_element_by_link_text("测试机"))
    #     expected_conditions.invisibility_of_element("my first")
    #     pass

    # def test_baidu(self):
    #     self.driver.get("https://www.baidu.com")
    #     expected_conditions.invisibility_of_element(self.driver.find_element(By.ID,"kw"))
    #     self.driver.find_element(By.ID,"kw").send_keys("霍格沃兹测试学院")
    #     expected_conditions.invisibility_of_element(self.driver.find_element(By.ID,"su"))
    #     self.driver.find_element(By.ID,"su").click()
    #     time.sleep(2)
    #
    # def test_case_click(self):
    #     element_click = self.driver.find_element_by_xpath("")
    #     element_rightclick = self.driver.find_element_by_xpath("")
    #     element_doubleclick = self.driver.find_element_by_xpath("")
    #     # 模拟PC端双击、右击、拖曳等
    #     action = ActionChains(self.driver)
    #     action.click(element_click)
    #     action.context_click(element_rightclick)
    #     action.double_click(element_doubleclick)
    #     action.perform()
    #
    # def test_movetoelement(self):
    #     self.driver.get("https://www.baidu.com")
    #     ele = self.driver.find_element_by_xpath("")
    #     action = ActionChains(self.driver)
    #     action.move_to_element(ele)
    #     action.perform()
    #
    # def test_dragdrop(self):
    #     self.driver.get("httpsL://www.baidu.com")
    #     drag_ele = self.driver.find_element_by_xpath("")
    #     drop_ele = self.driver.find_element_by_xpath("")
    #     action = ActionChains(self.driver)
    #     # 拖拽方法1
    #     action.drag_and_drop(drag_ele,drop_ele).perform()
    #     # 拖拽方法2
    #     # action.click_and_hold(drag_ele).release(drop_ele).perform()
    #     # 拖拽方法3
    #     # action.click_and_hold(drag_ele).move_to_element(drop_ele).release().perform()

    def test_touchAction(self):
        """
        打开firefox
        打开百度网页
        搜索框输入‘selenium测试’
        通过touchAction点击搜索框
        滑动到底部，点击下一页
        关闭firefox
        :return:
        """
        self.driver.get("http://www.baidu.com")
        expected_conditions.invisibility_of_element(self.driver.find_element(By.ID,'kw'))
        el = self.driver.find_element(By.ID,'kw')
        expected_conditions.invisibility_of_element(self.driver.find_element(By.ID,'su'))
        el_search = self.driver.find_element(By.ID,'su')
        el.send_keys('selenium测试')
        action = TouchActions(self.driver)
        action.tap(el_search)
        action.perform()
        action.scroll_from_element(el,0,10000).perform()


    def test_switchWindow(self):
        # 切换多窗口
        # 获取打开的所有窗口
        windows = self.driver.window_handles
        # 切换窗口至第一个
        self.driver.switch_to.window(window_name=windows[0])
        # 当前窗口
        current_window = self.driver.current_window_handle
        # 切换窗口至最后一个
        self.driver.switch_to.window(window_name=windows[-1])

    """
    frame存在两种：
    一种是嵌套的，一种是未嵌套的
    （1）处理未嵌套的iframe
        driver.switch_to_frame("frame的id")
        driver.switch_to_frame("frame-index")frame无ID的时候一句索引来处理，索引从0开始的driver.switch_to_frame(0)
    (2)处理嵌套的iframe
        对于嵌套的先进入到iframe的父节点，再进到子节点，然后可以对子节点里面的对象进行处理和操作
        driver.switch_to.frame(“父节点”)
        driver.switch_to.frame("子节点")
        
    """
    def test_switchFrame(self):
        # 根据元素id或index切换frame
        self.driver.switch_to.frame()
        # 切换到默认frame
        self.driver.switch_to.default_content()
        # 切换到父级frame
        self.driver.switch_to.parent_frame()











