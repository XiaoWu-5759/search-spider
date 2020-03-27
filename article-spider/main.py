# -*- coding: utf-8 -*-
'''
@createBy  :   xiaowu 
@date    :   2019/09/16 18:22:17
'''

from scrapy.cmdline import execute

import sys
import os

# print(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# 调用execute方法
execute(["scrapy", "crawl", "itcodemonkey"])