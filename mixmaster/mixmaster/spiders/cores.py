# -*- coding: utf-8 -*-

from scrapy          import Spider, Request
from mixmaster.items import Core


class Cores(Spider):
	name = 'cores'
	types = ['dragon', 'beast', 'bird', 'devil', 'insect', 'metal', 'mystic', 'plant']
	baseurl = 'http://formulasmixmaster.blogspot.com.br/p/{0}.html'

	def start_requests(self):
		urls = [self.baseurl.format(type) for type in self.types]

		for url in urls:
			yield Request(url, callback = self.parse)

	def parse(self, response):
		HENCH_SELECTOR = '//tbody/tr[@style = "height: 18.75pt;"]/..'

		for hench in response.xpath(HENCH_SELECTOR):
			NAME_SELECTOR = './tr/td[2]/div/strong/span/text()'

			item = Core()
			item['name'] = hench.xpath(NAME_SELECTOR).extract_first()

			yield item