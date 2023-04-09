import scrapy
from ..items import CacheimglinkItem
import time


class LinkcatchSpider(scrapy.Spider):
    name = 'linkcatch'
    start_urls = []
    start_urls.extend('http://admissions-duet.msappproxy.net/' for i in range(100))

    def parse(self,response):
        item = CacheimglinkItem()
        
        lnk = response.xpath('//div[@class ="form-group has-feedback"]/img/@src').get()
        item['lnk'] = lnk
        yield item
        # print("__________Links___________" , lnk)
        # if self.a <11:
        #     a += 1
        #     referesh = 'http://admissions-duet.msappproxy.net'
        #     # yield response.follow(referesh,callback=self.parse)
        # yield scrapy.follow(response.url,callback=self.parse)
        # scrapy.Request(response.url, callback=self.reload_url)

