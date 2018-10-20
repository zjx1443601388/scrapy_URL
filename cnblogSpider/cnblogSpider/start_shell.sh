#!/bin/bash
set -e

mysql_pass="jsdadv4g8t48sg"
scrapy_dir="/home/www/scrapy20180929/cnblogSpider/cnblogSpider/"

mysql -uhlspider -p$mysql_pass hlspider -e "truncate table starturl;"
mysql -uhlspider -p$mysql_pass hlspider -e "truncate table inner_spider_url;"
mysql -uhlspider -p$mysql_pass hlspider -e "truncate table out_spider_url;"

cd $scrapy_dir
time scrapy crawl  cnblogs >1 2>&1
python3 ipv4_url.py

echo "111"
