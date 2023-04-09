# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ImgxItem(scrapy.Item):
    # define the fields for your item here like:
    image_urls = scrapy.Field()
    images = scrapy.Field()
    imgname = scrapy.Field()
    imgdirectory = scrapy.Field()
    model = scrapy.Field()
    #########################################
    # modelnamebycatergory = scrapy.Field()
    ##########################################