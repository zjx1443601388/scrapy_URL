# -*- coding: utf-8 -*-
import scrapy
from cnblogSpider.items import CnblogspiderItem
from urllib.parse import urljoin, urlparse
import hashlib
class CnblogsComSpider(scrapy.Spider):
    name = 'cnblogs'
    allowed_domains = ['winiis.com']
   # start_urls = ['http://www.cnblogs.com/qiyeboy/default.html?page=1']
    start_urls = ['http://winiis.com/']
    ALL_urls = set()
    layer = 1
    url_list = {}
    inner_link = set()
    out_link = set()
    

    def parse(self, response):
        inner_link = None
        print("start_urls",self.start_urls)
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
            item['hash_start_link'] = hashlib.md5(b'self.start_urls[0]').hexdigest()

            if not link.startswith('http'):
                inner_link = link
                print("111: "+ str(inner_link)  + "==>from: " + str(response) )
                link = urljoin(self.start_urls[0],link)
            
            if urlparse(link).netloc != urlparse(self.start_urls[0]).netloc:
                print("外链" + link + "==>from: " + str(response))
                out_link = link
                inner_link = str()
                item['link'] = link + str(response)
               # item['from_link'] = str(response)
                yield item
            else:
                if inner_link:
                    item['link'] = inner_link + "内链" + str(response)
                else:
                    item['link'] = link + "内链" + str(response)
                    
                urls.add(link)
                print("内链" + link + "==>from: " + str(response) )
                #item['from_link'] = str(response)
            self.layer +=1
            print("layer",str(self.layer))

            yield item
        print("all_urls:"+ str(all_urls))
        new_urls = urls - self.ALL_urls
        urls_list = list(new_urls)
        self.ALL_urls = self.ALL_urls.union(urls)
       
        #print("内链:" + urls_list)
        for url in urls_list:
            print("0000:" + url)
            url = response.urljoin(url)
            yield scrapy.Request(url=url, callback=self.parse)


