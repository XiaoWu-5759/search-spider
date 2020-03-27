# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from datetime import datetime

import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose,TakeFirst

class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

def add_title(value):
    return value+"-xiaowu"

# 时间转换处理
def date_convert(value):
    try:
        create_time = datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
    except:
        create_time = datetime.now()
    return create_time

# 自定义ITemLoader
class JobBoleArticleItemLoader(ItemLoader):
    # 改写默认的output_processor
    default_output_processor = TakeFirst()

class ItcodemonkeyArticleItem(scrapy.Item):
    title = scrapy.Field(
        # 代表当item传入值的时候，我们可以对这些值进行一些预处理,MapCompose可以传入任意多个函数
        input_processor = MapCompose(lambda x: x+"-jobbole",add_title),
        # title上会添加-jobbole
    )
    create_time = scrapy.Field(
        input_processor=MapCompose(date_convert),
    )
    url = scrapy.Field()
    # url 通过md5 设置成固定长度
    url_object_id = scrapy.Field()
    classify = scrapy.Field()
    content = scrapy.Field()
