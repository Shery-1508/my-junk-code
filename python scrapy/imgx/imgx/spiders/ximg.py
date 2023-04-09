import scrapy


class XimgSpider(scrapy.Spider):
    name = 'ximg'
    model_name = "sia lust"  #"hazel moore"  #rinna ly , lily rader , chanel fenn , masha may , lexi belle
    # modifying name to use in the link an name  #
    modelnameinlink = model_name.lower().replace(' ','-')
    modelnameforscrap = model_name.title()
    #############################################
    start_urls = [f'https://sexhd.pics/gallery/{modelnameinlink}/1/',f'https://sexhd.pics/gallery/{modelnameinlink}/2/',f'https://sexhd.pics/gallery/{modelnameinlink}/3/'
                    ,f'https://sexhd.pics/gallery/{modelnameinlink}/4/',f'https://sexhd.pics/gallery/{modelnameinlink}/5/',f'https://sexhd.pics/gallery/{modelnameinlink}/6/'
                    f'https://sexhd.pics/gallery/{modelnameinlink}/7/',f'https://sexhd.pics/gallery/{modelnameinlink}/8/',]

    def parse(self, response):
        #getting galleries links of a model from a page
        gallerieslinks = response.xpath(f"(//div[@class='photo1']/a/p[contains(.,'{self.modelnameforscrap}')])/parent :: a/@href").getall()
        # print("galleries links : ",gallerieslinks)
        
        
        
        
        #parsing link to image extractor function
        for i in range(len(gallerieslinks)):
            yield response.follow(gallerieslinks[i],callback=self.extractimgs)
    
    def extractimgs(self,response):
        imgurls = response.xpath('.//*[contains(concat(" ",normalize-space(@class)," ")," relativetop ")]/following-sibling::*[1]/self::*[contains(concat(" ",normalize-space(@class)," ")," relativetop ")]/a/@href').getall()
        
        
        #####################################################################
        # modelnamebycatergory = response.xpath('//h2/a[1]/text()').get()
        ######################################################################
        
        
        
        filteredurls = []
        imgnames = []
        imgdirectory = []
        
        # for getting directory form url see site for clear obsevation
        namehelp = []
        namehelp = imgurls[1].split('/')
        imgdirectory.append(namehelp[-2])
        #################################################################
        
        # getting image names from urls
        for i in range(len(imgurls)):
            namehelp = []
            namehelp = imgurls[i].split('/')
            namefilter = namehelp[-2] + " " + namehelp[-1]
            imgnames.append(namefilter)
            # imgname.append()
        
        # relative to absolute urls
        for i in imgurls:
            filteredurls.append(response.urljoin(i))
        
        
        for i in range(len(filteredurls)):
        # for i in range(1):
            imglink = [filteredurls[i]]
            # print("thi is loop i: ",i,"  filtered :"  ,filteredurls[i],"  name :",imgnames[i])
            yield{
                
                
                ########################################################
                # 'modelnamebycatergory' : modelnamebycatergory,
                ########################################################
                
                
                "image_urls" : imglink,
                "imgname" : imgnames[i][:-4],
                "imgdirectory" : imgdirectory[0],
                "model" : self.modelnameforscrap,
            }
        