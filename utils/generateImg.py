#!/usr/bin/python
# -*- coding:utf8 -*-
from selenium import webdriver
from PIL import Image
import time
import uuid

WEBDRIVER_PATH = "/home/wildcat/usr/local/chromedriver/chromedriver"
HTML_TEMPLATE_PATH = 'file:///home/wildcat/PycharmProjects/imageGenerator/html/template.html'
IMAGE_PATH = '/home/wildcat/PycharmProjects/imageGenerator/img/'


# 开启webdriver
def openWebDriver(headlessflag=True):
    chrome_options = webdriver.ChromeOptions()
    if headlessflag:
        # 使用headless无界面浏览器模式
        chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(executable_path=WEBDRIVER_PATH, options=chrome_options)
    return driver


# 关闭webdriver
def closeWebDriver(driver):
    driver.quit


# 生成截图
def generateImg(driver):
    driver.get(HTML_TEMPLATE_PATH)
    title = driver.title
    print title
    full_image_name = '%s%s-%s.jpg' % (IMAGE_PATH, time.strftime('%Y%m%d', time.localtime()), uuid.uuid4())
    driver.save_screenshot(full_image_name)

    element = driver.find_element_by_id("pic")
    print(element.location)
    print(element.size)
    # 获取element的顶点坐标
    xPiont = element.location['x']
    yPiont = element.location['y']
    # 获取element的宽、高
    element_width = xPiont + element.size['width']
    element_height = yPiont + element.size['height']

    picture = Image.open(full_image_name)
    picture = picture.crop((xPiont, yPiont, element_width, element_height))
    res_img_name = '%s%s-%s_res.jpg' % (IMAGE_PATH, time.strftime('%Y%m%d', time.localtime()), uuid.uuid4())
    picture.save(res_img_name)
    return 'ok'
