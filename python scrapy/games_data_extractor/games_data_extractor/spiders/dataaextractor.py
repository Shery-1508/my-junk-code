import scrapy
from ..items import GamesDataExtractorItem


class DataExtractorSpider(scrapy.Spider):
    name = 'dataaextractor'
    start_urls = ['http://ebravo.pk/beta/games']
    
    def parse(self, response):
        Items = GamesDataExtractorItem()
        
        title = response.xpath('(//div[@class = "video-title"])/a/text()').getall()
        upload_date = response.css('div.video-page.text-success::text').getall()
        
        ###################  Filtering date list #############################################
        for s in range(0,len(upload_date)):
            upload_date[s] = upload_date[s].replace("\r\n","")
            upload_date[s] = upload_date[s].strip()
        while("" in upload_date) :
            upload_date.remove("")
        #######################################################################################
        
        # checking to make sure data
        if len(title) == len(upload_date):
            for x in range(0,len(title)):
                Items['title'] = title[x]
                Items['upload_date'] = upload_date[x]
                yield Items
        
        nextpage = response.xpath('//a[@title ="Next"]/@href').get()
        
        if nextpage is not None:
            yield response.follow(nextpage, callback=self.parse)
        
        