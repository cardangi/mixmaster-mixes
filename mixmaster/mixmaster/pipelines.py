from json                    import dumps
from scrapy                  import Request
from scrapy.pipelines.images import ImagesPipeline

class JsonWriterPipeline(object):
    def open_spider(self, spider):
        self.file = open('cores.jl', 'wb')

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        line = dumps(dict(item)) + "\n"
        self.file.write(line.encode())
        return item

class MyImagesPipeline(ImagesPipeline):
	def get_media_requests(self, item, info):
		if 'image_urls'	in item.keys(): # Checa se é o item correto
			for image_url in item['image_urls']:
				yield Request(image_url, meta={'item': item})

	def file_path(self, request, response = None, info = None):
		item = request.meta['item']
		image_guid = request.url.split('/')[-1]
		
		return 'cores/{0}.jpg'.format(item['id'])
