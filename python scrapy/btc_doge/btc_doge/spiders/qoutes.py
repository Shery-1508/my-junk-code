import scrapy

class qoutes(scrapy.Spider):
    name = 'qoutes'
    start_urls = ['https://quotes.toscrape.com/']
    
    def parse(self, response):

        quotesss = response.css('.quote')
        for quote in quotesss:
            title = quote.css('.text::text').get()
            author = quote.css('.author::text').get()
            tags = quote.css('.tags .tag::text').getall()
            yield {
                'title': title,
                'author': author,
                'tags': tags
            }

    # def parse(self,response):
    #     QUOTE = response.xpath('//div[@class = "qoute"]')
    #     for q in QUOTE:
    #         quote = q.xpath('//span[@class = "text"]/text()').get()
    #         author = q.xpath('//*[@class = "author"]/text()').get()
    #         tags = q.xpath('//div[@class = "tags"]/a[@class = "tag"]/text()').getall()
    #         yield { 
    #             'Qoute'  : quote ,
    #             'Author' : author ,
    #             'Tags'   : tags,
    #         }