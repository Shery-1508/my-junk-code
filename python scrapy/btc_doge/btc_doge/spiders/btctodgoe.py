import scrapy


class BtctodgoeSpider(scrapy.Spider):   
    name = 'btctodgoe'
    allowed_domains = ['www.google.com']
    start_urls = ['https://www.google.com/finance/quote/BTC-DOGE']

    def parse(self, response):
        return {'title': response.xpath('//div[@class = "YMlKec fxKbKc"]/text()').get()}
