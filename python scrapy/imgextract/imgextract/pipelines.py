from scrapy.pipelines.images import ImagesPipeline

class imagedownloaderpipeline(ImagesPipeline):
        def file_path(self, request, response=None, info=None, *, item=None):
            imagenmes = item['gamename']
            # image_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
            return f'full/{imagenmes}.jpg'