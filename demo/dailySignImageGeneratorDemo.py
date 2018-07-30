#!/usr/bin/python
# -*- coding:utf8 -*-

from selenium import webdriver
import os
from PIL import Image

chrome_options = webdriver.ChromeOptions()
# 使用headless无界面浏览器模式
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver1 = webdriver.Chrome(executable_path="/home/user/usr/local/chromedriver/chromedriver", options=chrome_options)
driver1.get("file:///home/user/project/self/pythonproject/imageGenerator/html/DailySignHtml/html/index3.html")
# driver1.get("http://www.baidu.com")
data = driver1.title
full_image = '/home/user/project/self/pythonproject/imageGenerator/img/index3.png'
driver1.save_screenshot(full_image)

element = driver1.find_element_by_id("pic")
print(element.location)
print(element.size)
# 获取element的顶点坐标
xPiont = element.location['x']
yPiont = element.location['y']
# 获取element的宽、高
element_width = xPiont + element.size['width']
element_height = yPiont + element.size['height']

picture = Image.open(full_image)
res_image = '/home/user/project/self/pythonproject/imageGenerator/img/index3_res.png'
picture = picture.crop((xPiont, yPiont, element_width, element_height))
picture.save(res_image);

print data
print os.getcwd()
driver1.close()
