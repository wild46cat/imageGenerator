#!/usr/bin/python
# -*- coding:utf8 -*-

from selenium import webdriver
import os
from PIL import Image

BASE_DIR = '/Users/wuxueyou/Project/python/imageGenerator'
driver_path = '%s/deploy/docker/chromedriverformac' % BASE_DIR
if __name__ == '__main__':
    print(driver_path)
    chrome_options = webdriver.ChromeOptions()
    # 使用headless无界面浏览器模式
    # chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    driver1 = webdriver.Chrome(executable_path=driver_path, options=chrome_options)
    driver1.get("file://%s/resources/html/template.html" % BASE_DIR)
    # driver1.get("http://www.baidu.com")
    data = driver1.title
    full_image = '%s/resources/img/template.png' % BASE_DIR
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
    res_image = '%s/resources/img/template_res.png' % BASE_DIR
    picture = picture.crop((xPiont, yPiont, element_width, element_height))
    picture.save(res_image);

    print data
    print os.getcwd()
    driver1.close()
