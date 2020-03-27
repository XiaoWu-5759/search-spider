# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from urllib import parse
from datetime import datetime
from scrapy.loader import ItemLoader

from ArticleSpider.items import ItcodemonkeyArticleItem, JobBoleArticleItemLoader
from ArticleSpider.util.common import get_md5

# 继承spider
class ItcodemonkeySpider(scrapy.Spider):
    name = 'itcodemonkey'
    allowed_domains = ['www.itcodemonkey.com']
    start_urls = ['https://www.itcodemonkey.com/p/153/']

    def parse(self, response):
        # 1. 获取文章列表页中的文章url 并交给scrapy下载后解析函数进行具体字段解析
        # 2. 获取下一页的url并交给scrapy进行下载 下载完成后交给parse

        # 解析列表页中的所有文章url 并交给scrapy下载后并进行解析
        post_urls = response.css('div.list-boxes > h2 > a::attr(href)').extract()
        for post_url in post_urls:
            # post_url = response.url + post_url
            yield Request(url = parse.urljoin(response.url,post_url), callback=self.parse_detail)
            # print(post_url.extract())
        
        # 提取下一页并交给 scrapy下载
        current_page = response.css('li.active.current > span::text').extract_first("")
        # 直到没有 下一页，爬虫结束
        if(current_page):
            # 空 无法强转
            current_page = int(current_page)
            next_page = '/p/{0}/'.format(current_page+1)
            yield Request(url = parse.urljoin(response.url,next_page), callback = self.parse)

    def parse_detail(self, response):
        article_item = ItcodemonkeyArticleItem()
        # 提取文章的具体字段
        item_loader = JobBoleArticleItemLoader(item=ItcodemonkeyArticleItem(),response=response)
        # 针对css选择器
        item_loader.add_css('title','body > div.container.tc-main > div.row > div.span9 > div > h2::text')
        item_loader.add_css('create_time', 'body > div.container.tc-main > div.row > div.span9 > div > div.article-infobox > span::text')
        item_loader.add_css('classify','body > div.container.tc-main > div.row > div.span9 > div > div.article-infobox > span > a::text')
        item_loader.add_css('content', '#article_content')
        # 针对直接取值的情况
        item_loader.add_value('url', response.url)
        item_loader.add_value('url_object_id', get_md5(response.url))
        article_item = item_loader.load_item()
        yield article_item
