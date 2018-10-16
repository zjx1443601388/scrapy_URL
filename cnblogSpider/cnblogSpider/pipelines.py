# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import pymongo
from scrapy.exceptions import DropItem
from scrapy import log
import pymysql
import pymysql.cursors
import codecs
from twisted.enterprise import adbapi

class CnblogspiderPipeline(object):
    def __init__(self):
        self.ids_seen = set()
    def process_item(self, item, spider):
        if item['link']:
            if item['link'] in self.ids_seen:
                raise DropItem("Duplicate item found: %s" % item)
            else:
                self.ids_seen.add(item['link'])
        if item['start_link']:

            if item['start_link'] in self.ids_seen:
                raise DropItem("Duplicate item found: %s" % item)
            else:
                self.ids_seen.add(item['start_link'])
        if item['hash_start_link']:

            if item['hash_start_link'] in self.ids_seen:
                raise DropItem("Duplicate item found: %s" % item)
            else:
                self.ids_seen.add(item['hash_start_link'])

        if not item['from_link']:
            raise DropItem("Duplicate item found: %s" % item)
            
        return item


class MongoPipeline(object):
    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DB')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def process_item(self, item, spider):
        name = item.__class__.__name__
        self.db[name].insert(dict(item))
        return item

    def close_spider(self, spider):
        self.client.close()


class WebcrawlerScrapyPipeline(object):
    @classmethod
    def from_settings(cls, settings):
        dbargs = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            passwd=settings['MYSQL_PASSWD'],
            port=settings['MYSQL_PORT'],
            charset='utf8',
            cursorclass=pymysql.cursors.DictCursor,
            use_unicode=True,
        )
        dbpool = adbapi.ConnectionPool('pymysql', **dbargs)
        return cls(dbpool)

    def __init__(self,dbpool):
        self.dbpool=dbpool


    def process_item(self, item, spider):
        d=self.dbpool.runInteraction(self._conditional_insert, item, spider)#调用插入的方法
        log.msg("-------------------连接好了-------------------")
        d.addErrback(self._handle_error,item,spider)#调用异常处理方法
        d.addBoth(lambda _: item)
        return d

    def _conditional_insert(self, conn, item, spider):
        log.msg("-------------------打印-------------------")

        #if not conn.execute("select hash_start_link from starturl where start_url= %s",(item['hash_start_link'])):
        conn.execute("insert into StartUrl (hash_start_link , start_url) values(%s, %s)",
                     (item['hash_start_link'], item['start_link']))
        log.msg("-------------------一轮循环完毕-------------------")
    def _handle_error(self, failue, item, spider):
        print(failue)
