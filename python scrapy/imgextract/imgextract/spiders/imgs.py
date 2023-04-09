import scrapy


class ImgsSpider(scrapy.Spider):
    name = 'imgs'
    start_urls = ['http://ebravo.pk/beta/games']

    def parse(self, response):
        junkurls = response.xpath("//div[@class = 'video-card-image']/a[1]/@href").getall()
        for lnk in junkurls:
            yield response.follow(lnk , callback = self.objectparse)
        
        
        nextpage = response.xpath("//li[@class='page-item']/a[@title='Next']/@href").get()
        if nextpage:
            yield response.follow(nextpage,callback=self.parse)
    
    
    
    def objectparse(self,response):
        junkimglink = response.xpath("//div[@class = 'film-poster mb-2']/img/@src").getall()
        gamename = response.xpath("//div[@class = 'film-poster mb-2']/img/@title").get()
        imglink = []
        
        while ' ' in gamename:
            gamename = gamename.replace(' ','-')
        for lnk in junkimglink:
            imglink.append(response.urljoin(lnk))
        
        
        yield { "image_urls" : imglink,
                "gamename"   : gamename,
                }
        