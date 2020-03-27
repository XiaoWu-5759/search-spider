# -*- coding: utf-8 -*-
__author__ = 'xiaowu'

import re

line = "x00000000000000000000xxowu5759"
regex_str = ".*?(x.*?x).*"
match_obj = re.match(regex_str, line)
if match_obj:
    print(match_obj.group(1))