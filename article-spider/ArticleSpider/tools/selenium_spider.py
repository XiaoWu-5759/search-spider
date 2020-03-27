# -*- coding: utf-8 -*-
'''
@createBy  :   xiaowu 
@date    :   2019/11/01 11:15:22
'''

from selenium import webdriver
from scrapy.selector import Selector
# 可以设置参数 executable_path = '驱动地址'
browser = webdriver.Chrome()
# browser.get('https://www.baidu.com')

# print(browser.page_source)
# t_selector = Selector(text=browser.page_source)
# t_selector.css('')

# browser.get('https://www.zhihu.com/signin')

# browser.find_element_by_css_selector('div.SignFlow-tabs > div:nth-child(2)').click()

# # 账号
# browser.find_element_by_css_selector('div.SignFlow-account > div > label > input').send_keys('18895386003')
# # 密码
# browser.find_element_by_css_selector('div.SignFlow-password > div > label > input').send_keys('961119101125')
# # 点击按钮
# browser.find_element_by_css_selector('div.Card.SignContainer-content > div > form > button').click()

# browser.get('https://www.weibo.com/login.php')

# browser.maximize_window()
# # 账号
# browser.find_element_by_css_selector('#loginname').send_keys('18895386003')
# # 密码
# browser.find_element_by_css_selector('#pl_login_form > div > div:nth-child(3) > div.info_list.password > div > input').send_keys('961119101125')
# # 点击登录
# # 有时候js，页面没有加载完成，点击和查找是失败的
# import time
# time.sleep(10)
# browser.find_element_by_css_selector('#pl_login_form > div > div:nth-child(3) > div.info_list.login_btn > a').click()

# 开源中国博客
browser.get('https://www.oschina.net/blog')
# 执行js代码
import time
time.sleep(10)
for _ in range(3):
    browser.execute_script('window.scrollTo(0, document.body.scrollHeight); var lenOfPage=document.body.scrollHeight; return lenOfPage;')
    time.sleep(3)