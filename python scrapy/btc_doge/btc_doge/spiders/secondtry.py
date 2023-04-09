import scrapy


class SecondtrySpider(scrapy.Spider):
    name = 'secondtry'
    allowed_domains = ['bscsshery96.coolpage.biz']
    start_urls = ['https://bscsshery96.coolpage.biz/HTML/Philosophy.html']

    def parse(self, response):
        return {"title" : response.xpath('//div/ol/li/text()').getall()}
