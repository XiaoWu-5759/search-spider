# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs  # 编码
import json

from scrapy.pipelines.images import ImagesPipeline
from scrapy.exporters import JsonItemExporter
from twisted.enterprise import adbapi

import pymysql



class ArticlespiderPipeline(object):
    def process_item(self, item, spider):
        return item

# 拦截并保存 item                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
class JsonWithEncodingPipeline(object):
    # 自定义json文件的导出
    def __init__(self):
        self.file = codecs.open('article.json','w',encoding='utf-8')
    
    def process_item(self, item, spider):
        lines = json.dumps(dict(item), ensure_ascii=False)
        self.file.write(lines)
        return item
    
    def close_spider(self, spider):
        print('close')
        self.file.close()

class JsonExporterPipeline(object):
    # 调用scrapy提供的json export到处json文件
    def __init__(self):
        self.file = open('articleexport.json','wb')
        self.exporter = JsonItemExporter(self.file,encoding='utf-8',ensure_ascii=False)
        self.exporter.start_exporting()
    
    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
    
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

class MysqlPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect('localhost','root','123456','spider', charset = 'utf8')
        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        insert_sql = """
            insert into t_spider_article(article_title,article_create_time,article_url,article_url_object_id,article_classify,article_content)
            values (%s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(insert_sql, (item['title'],item['create_time'],item['url'],item['url_object_id'],item['classify'],item['content']))
        self.conn.commit()  # 增 删 改都需要 提交
    
    def close_spider(self, spider):
        print('mysql close')
        self.conn.close()

class MysqlTwistedPipeline(object):

    @classmethod
    # 这里可以读取到 setting设置文件
    def from_settings(cls, settings):
        db_params = dict(
            host = settings['MYSQL_HOST'],
            database = settings['MYSQL_DBNAME'],
            user = settings['MYSQL_USER'],
            password = settings['MYSQL_PASSWORD'],
            charset = 'utf8'
        )
        # 不能选择 MySQLdb
        dbpool = adbapi.ConnectionPool('pymysql', **db_params)
        # 实例化一个对象
        return cls(dbpool)
    
    # 在启动函数的时候，就已经调用了
    def __init__(self, dbpool):
        self.dbpool = dbpool

    def process_item(self, item, spider):
        # 使用twisted将mysql插入变成异步执行
        # 使用Twisted将mysql插入变成异步执行
        # runInteraction可以将传入的函数变成异步的
        query = self.dbpool.runInteraction(self.do_insert, item)
        query.addErrback(self.handle_error,item, spider)

    # 异步错误处理函数
    def handle_error(self,failure,item,spider):
        # 处理异步插入异常
        print(failure)

    def do_insert(self, cursor, item):
        # 执行具体的插入
        insert_sql = """
            insert into t_spider_article(article_title,article_create_time,article_url,article_url_object_id,article_classify,article_content)
            values (%s, %s, %s, %s, %s, %s)
        """
        cursor.execute(insert_sql, (item['title'],item['create_time'],item['url'],item['url_object_id'],item['classify'],item['content']))


class ArticleImagePipeline(ImagesPipeline):
    def item_completed(self, results, item, info):
        for ok, value in results:
            image_file_path = value['path']
        item['font_image_path'] = image_file_path
        return item
