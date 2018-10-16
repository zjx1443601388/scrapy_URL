# -*- coding: utf-8 -*-
import scrapy


class JandanNetSpider(scrapy.Spider):
    name = 'jandan.net'
    allowed_domains = ['http://jandan.net/ooxx']
    start_urls = ['http://http://jandan.net/ooxx/']

    def parse(self, response):
        pass

from cnblogSpider.items import JiandanItem
class jiandanSpider(scrapy.Spider):
    name = 'jiandan'
    allowed_domains = []
    start_urls = ["http://jandan.net/ooxx"]
     
    def parse(self, response):
        item = JiandanItem()
        item['image_urls'] = response.xpath('//img//@src').extract()#提取图片链接
        print ('image_urls',item['image_urls'])
        new_url= response.xpath('//a[@class="previous-comment-page"]//@href').extract_first()#翻页
        url = response.urljoin(new_url)
        print ('new_url',new_url)
        if new_url:
            yield scrapy.Request(url,callback=self.parse)
