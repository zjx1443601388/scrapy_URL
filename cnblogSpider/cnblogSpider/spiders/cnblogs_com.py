# -*- coding: utf-8 -*-
import scrapy
from cnblogSpider.items import CnblogspiderItem
from urllib.parse import urljoin, urlparse
import hashlib
import re
from bs4 import BeautifulSoup
class CnblogsComSpider(scrapy.Spider):
    name = 'cnblogs'
    allowed_domains = ['winiis.com']
   # start_urls = ['http://www.cnblogs.com/qiyeboy/default.html?page=1']
    start_urls = ['http://winiis.com/']
    ALL_urls = set()
    ALL_urls.add(start_urls[0])
    layer = 1
    url_list = {}
    inner_link = set()
    out_link = set()
    

    def html_label(self, lable1):
        if self.lable1 == "<a":
            return 1
        elif self.lable1 == "<link":
            return 2
        elif self.lable1 == "<script":
            return 3
        elif self.lable1 == "<img":
            return 4
        elif self.lable1 == "<video":
            return 5
        else:
            return 6

    def parse(self, response):
        inner_link = str()
       # print("start_urls",self.start_urls)
      #  all_urls = set()
        urls = set()
        all_urls= set()
      #  print(self.start_urls[0])
        all_link = response.xpath("//*//@src | //*//@href | //*//@url |  //*//@ocde" ).extract() #页面内的所有链接
        #item = CnblogspiderItem()
        
        
        for link in all_link:
            all_urls.add(link)
            item = CnblogspiderItem()
            item['start_link'] = self.start_urls[0]
            item['hash_start_link'] = hashlib.md5(self.start_urls[0].encode("gb2312")).hexdigest()
            item['from_link'] = str(response.url)
            print("meta11:"+ str(response.meta['depth'] + 1))
            item['layer'] = response.meta['depth'] + 1

            soup = BeautifulSoup(response.text,"lxml")
            href = soup.find_all(attrs={"href": link})
            if href != []:
                href_s = str(href[0])
                data = href_s.split()[0]
                print("dada" + data)
                
                if data == "<a":
                    url_lable = 1
                elif data == "<link":
                    soup1 = BeautifulSoup(href_s,'lxml')
                    if soup1.link['type'] == "text/css":
                        url_lable = 2
                    elif soup1.link['type'] == "image/x-icon":
                        url_lable = 4
                    else:
                        url_lable = 6
                elif data == "<script":
                    url_lable = 3
                elif data == "<img":
                    url_lable = 4
                elif data == "<video":
                    url_lable = 5
                else:
                    url_lable = 6


            else:
                src = soup.find_all(attrs={"src": link})
                if src != []:
                    src_s = str(src[0])
                    data = str(src_s.split()[0])
                    if data == "<a":
                        url_lable = 1
                    elif data == "<link":
                        url_lable = 2
                    elif data == "<script":
                        url_lable = 3
                    elif data == "<img":
                        url_lable = 4
                    elif data == "<video":
                        url_lable = 5
                    else:
                        url_lable = 6


                    
                else:
                    url_lable = 6
            print("url_lable: "+ link + "11" + str(url_lable))
            item['type1'] = url_lable

             

                

            if not link.startswith('http'):
                inner_link = link
            #    print("111: "+ str(inner_link)  + "==>from: " + str(response) )
                link = urljoin(self.start_urls[0],link)
            
            if urlparse(link).netloc != urlparse(self.start_urls[0]).netloc:
                print("外链" + link + "==>from: " + str(response))
                out_link = link
                inner_link = str()
                item['out_link'] = link
               # item['from_link'] = str(response)
                item['out_link_hash'] = hashlib.md5(link.encode("gb2312")).hexdigest()
                item['inner_link'] = None
                yield item
            else:
                if inner_link:
                    item['inner_link'] = inner_link
                    item['inner_link_hash'] = hashlib.md5(inner_link.encode("gb2312")).hexdigest()
                else:
                    item['inner_link'] = link 
                    item['inner_link_hash'] = hashlib.md5(link.encode("gb2312")).hexdigest()
                
                item['out_link'] = None
                print("link111" + link)
                urls.add(link)
                print("内链" + link + "==>from: " + str(response) )
                #item['from_link'] = str(response)
            self.layer +=1
         #   print("layer",str(self.layer))
            print("out_link:" + str(item['out_link']))


            yield item
        print("all_urls:"+ str(self.ALL_urls))

        new_urls = urls - self.ALL_urls
        urls_list = list(new_urls)
        #print("new_urls" + urls_list)
        self.ALL_urls = self.ALL_urls.union(urls)
       
        #print("内链:" + urls_list)
        for url in urls_list:
            #print("0000:" + url)
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse)


