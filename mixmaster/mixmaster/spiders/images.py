# -*- coding: utf-8 -*-

from scrapy          import Spider, Request
from mixmaster.items import ImageCore
from re              import match

class Cores(Spider):
	name = 'images'
	types = ['dragon', 'beast', 'bird', 'devil', 'insect', 'metal', 'mystic', 'plant']
	baseurl = 'http://formulasmixmaster.blogspot.com.br/p/{0}.html'

	def start_requests(self):
		urls = [self.baseurl.format(type) for type in self.types]

		for url in urls:
			yield Request(url, callback = self.parse)

	def parse(self, response):
		IMAGE_SELECTOR = '//img/@src'

		for imageurl in response.xpath(IMAGE_SELECTOR):
			if 'monster' in imageurl.extract():
				imageurl = imageurl.extract()
				image = ImageCore()

				image['image_urls'] = [imageurl]
				image['id']         = imageurl[imageurl.find("monster")+7 : imageurl.find(".gif")]

				yield image