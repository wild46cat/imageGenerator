#!/usr/bin/python
# -*- coding:utf8 -*-
from selenium import webdriver
from PIL import Image
import time
import uuid
import os
import sys
import logging
import logging.config

# WORK_SPACE = '/space/imageGenerator'
WORK_SPACE = '/home/wildcat/project/pythonproject/imageGenerator'
WEBDRIVER_PATH = r"%s/deploy/docker/chromedriver" % WORK_SPACE
HTML_TEMPLATE_PATH = 'file://%s/resources/html/template.html' % WORK_SPACE
IMAGE_PATH = '%s/resources/img/' % WORK_SPACE

# 读取日志配置文件内容
logging.config.fileConfig('%s/resources/logging.conf' % WORK_SPACE)

# 创建一个日志器logger
logger = logging.getLogger('generateImg')


# 开启webdriver
def openWebDriver(headlessflag=True):
    logger.info("work_space %s" % os.getcwd())
    chrome_options = webdriver.ChromeOptions()
    if headlessflag:
        # 使用headless无界面浏览器模式
        chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(executable_path=WEBDRIVER_PATH, options=chrome_options)
    return driver


# 关闭webdriver
def closeWebDriver(driver):
    driver.quit


# 生成截图
def generateImg(driver):
    driver.get(HTML_TEMPLATE_PATH)
    title = driver.title
    full_image_name = '%s%s-%s.png' % (IMAGE_PATH, time.strftime('%Y%m%d', time.localtime()), uuid.uuid4())
    driver.save_screenshot(full_image_name)

    element = driver.find_element_by_id("pic")
    logger.info("element info:%s,%s" % (element.location, element.size))
    # 获取element的顶点坐标
    xPiont = element.location['x']
    yPiont = element.location['y']
    # 获取element的宽、高
    element_width = xPiont + element.size['width']
    element_height = yPiont + element.size['height']

    picture = Image.open(full_image_name)
    picture = picture.crop((xPiont, yPiont, element_width, element_height))
    res_img_name = '%s_res.png' % full_image_name[:-4]
    picture.save(res_img_name)
    return 'ok'
