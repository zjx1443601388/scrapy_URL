#/usr/bin/env python
# -*- coding: utf-8 -*-


import pymysql
import re
from urllib.parse import urljoin, urlparse
from os import popen
import sys

start_url = ['http://winiis.com/']





#if a ip return True,else False
def isIP(str):
    p = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
    if p.match(str):
        return True
    else:
        return False

def ipv6_addr(addr):
        '''
        Returns True if the IPv6 address (and optional subnet) are valid, otherwise
        returns False.
        '''
        # From http://stackoverflow.com/questions/6276115/ipv6-regexp-python
        ip6_regex = (r'(\A([0-9a-f]{1,4}:){1,1}(:[0-9a-f]{1,4}){1,6}\Z)|'
                     r'(\A([0-9a-f]{1,4}:){1,2}(:[0-9a-f]{1,4}){1,5}\Z)|'
                     r'(\A([0-9a-f]{1,4}:){1,3}(:[0-9a-f]{1,4}){1,4}\Z)|'
                     r'(\A([0-9a-f]{1,4}:){1,4}(:[0-9a-f]{1,4}){1,3}\Z)|'
                     r'(\A([0-9a-f]{1,4}:){1,5}(:[0-9a-f]{1,4}){1,2}\Z)|'
                     r'(\A([0-9a-f]{1,4}:){1,6}(:[0-9a-f]{1,4}){1,1}\Z)|'
                     r'(\A(([0-9a-f]{1,4}:){1,7}|:):\Z)|(\A:(:[0-9a-f]{1,4})'
                     r'{1,7}\Z)|(\A((([0-9a-f]{1,4}:){6})(25[0-5]|2[0-4]\d|[0-1]'
                     r'?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3})\Z)|'
                     r'(\A(([0-9a-f]{1,4}:){5}[0-9a-f]{1,4}:(25[0-5]|2[0-4]\d|'
                     r'[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3})\Z)|'
                     r'(\A([0-9a-f]{1,4}:){5}:[0-9a-f]{1,4}:(25[0-5]|2[0-4]\d|'
                     r'[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}\Z)|'
                     r'(\A([0-9a-f]{1,4}:){1,1}(:[0-9a-f]{1,4}){1,4}:(25[0-5]|'
                     r'2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d))'
                     r'{3}\Z)|(\A([0-9a-f]{1,4}:){1,2}(:[0-9a-f]{1,4}){1,3}:'
                     r'(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?'
                     r'\d?\d)){3}\Z)|(\A([0-9a-f]{1,4}:){1,3}(:[0-9a-f]{1,4})'
                     r'{1,2}:(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|'
                     r'[0-1]?\d?\d)){3}\Z)|(\A([0-9a-f]{1,4}:){1,4}(:[0-9a-f]'
                     r'{1,4}){1,1}:(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|'
                     r'2[0-4]\d|[0-1]?\d?\d)){3}\Z)|(\A(([0-9a-f]{1,4}:){1,5}|:):'
                     r'(25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?'
                     r'\d?\d)){3}\Z)|(\A:(:[0-9a-f]{1,4}){1,5}:(25[0-5]|2[0-4]\d|'
                     r'[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}\Z)')
        return bool(re.match(ip6_regex, addr))

def  isexist(data):
    num = 0
    for  i  in range(0,len(data)):
        new_data = ''.join(data[i].split())
        if len(re.findall(":", new_data)) > 1:
            num +=1
    return num





def popen_pro(cmd):
	popen_pro=popen(cmd)
	popen_data=popen_pro.readlines()
	popen_pro.close()
	return popen_data


    #MySQL连接
def mysql_link():
    mysql_user = 'hlspider',
    mysql_pass = 'jsdadv4g8t48sg',
    mysql_host = '127.0.0.1',
    mysql_port = 3306,
    mysql_db = 'hlspider'


    connect = pymysql.connect(
            user = mysql_user[0],
            password = mysql_pass[0],
            db = mysql_db,
            host = mysql_host[0],
            port = mysql_port[0],
            charset = 'utf8'
            )

    return connect

def url_is_AAAA(url_data, url_count=0):


    connect = mysql_link()
    con = connect.cursor()



    count = 0
    for url in url_data:


        domain = urlparse(url[0]).netloc.split(':')[0]

        if isIP(domain):
            update_sql = "update out_spider_url set isip=%s where out_url='%s'; " % (1, url[0])
            con.execute(update_sql)
            update_sql_1 = "update out_spider_url set isAAAA=%s where out_url='%s'; " % (0, url[0])
            con.execute(update_sql_1)
        else:
            update_sql = "update out_spider_url set isip=%s where out_url='%s'; " % (0, url[0])
            con.execute(update_sql)

            cmd = "dig '%s' AAAA +short" %domain
            res = popen_pro(cmd)
            if res == []:
                update_sql = "update out_spider_url set isAAAA=%s where out_url='%s'; " % (0, url[0])
                con.execute(update_sql)
            else:

                #resturn = ''.join(res[0].split())
                m = isexist(res)
                if m > 0:
                    update_sql = "update out_spider_url set isAAAA=%s where out_url='%s'; " % (1, url[0])
                    con.execute(update_sql)
                else:
                    update_sql = "update out_spider_url set isAAAA=%s where out_url='%s'; " % (0, url[0])
                    con.execute(update_sql)





        count +=1


    con.close()






def url_link():
    select_out_url = "select out_url from out_spider_url;"
    select_sql_layer2 = "select distinct out_url from spider_url where out_url is not  NULL and layer=2;"
    select_sql_layer3 = "select distinct out_url from spider_url where out_url is not  NULL and layer=3;"
    delete_sql="delete  from spider_url where layer =2 and from_url=(select start_url from starturl);"
    try:
        connect = mysql_link()
        con = connect.cursor()
        con.execute(select_out_url)
        #mysql获取数据
        layer1_count = con.execute(select_out_url)
        layer1_data=con.fetchall()
        url_is_AAAA(layer1_data)


    except Exception as e:
        print(e)
        exit(1)
    finally:
        con.close()



if __name__ == '__main__':
    url_link()







