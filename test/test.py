#!/usr/bin/python
# -*- coding:utf8 -*-
import datetime
import time

t1 = time.mktime(datetime.datetime.now().timetuple())
t2 = time.mktime(datetime.datetime.now().timetuple())
print(t2 - t1)
