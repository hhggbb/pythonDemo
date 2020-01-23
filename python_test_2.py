from selenium import webdriver
import datetime
now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
# 打开Chrome浏览器
browser = webdriver.Chrome()
# 打开淘宝
browser.get("https://www.taobao.com")
# 点击登录
browser.find_element_by_link_text("亲，请登录").click()
# 打开购物车
browser.get("https://cart.taobao.com/cart.htm")
# 购物车全选
browser.find_element_by_id("J_SelectAll1").click()
# 点击结算
browser.find_element_by_link_text("结 算").click()
# 提交订单
browser.find_element_by_link_text('提交订单').click()