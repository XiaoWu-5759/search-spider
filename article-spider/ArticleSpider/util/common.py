# -*- coding: utf-8 -*-
'''
@createBy  :   xiaowu 
@date    :   2019/10/31 10:54:52
'''

import hashlib

def get_md5(url):
    if isinstance(url,str):
        url = url.encode("utf-8")
    m = hashlib.md5()
    m.update(url)
    return m.hexdigest() # md5的摘要生成

if __name__ == "__main__":
    print(get_md5("http://bole.com"))