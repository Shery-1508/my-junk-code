import scrapy


class AgaintrySpider(scrapy.Spider):
    name = 'againtry'
    allowed_domains = ['ebravo.pk']
    start_urls = ['http://ebravo.pk/beta/games']

    def parse(self, response):
        return {"tilesss" : response.xpath('//div[@class = "video-title"]/a/text()').getall()}