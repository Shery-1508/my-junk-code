from scrapy.pipelines.images import ImagesPipeline

class ximgextract(ImagesPipeline):
    def file_path(self, request, response=None, info=None, *, item=None):
        image_name = item['imgname']
        image_directory = item['imgdirectory']
        model = item['model']
                
        ####################################################
        # modelnamebycatergory = item['modelnamebycatergory']
        # return f'{model}/{modelnamebycatergory}/{image_directory}/{image_name}.jpg'
        ####################################################
        
        # return f'{model}/{image_name}.jpg'
        return f'{model}/{image_directory}/{image_name}.jpg'