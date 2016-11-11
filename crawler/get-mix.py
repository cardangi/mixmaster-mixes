# -*- coding: utf-8 -*-

import scrapy

class getmix(scrapy.Spider):
	name = 'getmixes'
	start_urls = ['http://formulasmixmaster.blogspot.com.br/p/dragon.html', 
				  'http://formulasmixmaster.blogspot.com.br/p/beast.html',
				  'http://formulasmixmaster.blogspot.com.br/p/bird.html',
				  'http://formulasmixmaster.blogspot.com.br/p/devil.html',
				  'http://formulasmixmaster.blogspot.com.br/p/insect.html',
				  'http://formulasmixmaster.blogspot.com.br/p/metal.html',
				  'http://formulasmixmaster.blogspot.com.br/p/mystic.html',
				  'http://formulasmixmaster.blogspot.com.br/p/plant.html']

	def parse(self, response):
		HENCH_SELECTOR = '//tbody/tr[@style = "height: 18.75pt;"]/..'

		for hench in response.xpath(HENCH_SELECTOR):
			NAME_SELECTOR = './tr/td[2]/div/strong/span/text()'
			LEVEL_SELECTOR = './tr/td[4]/div/span/text()'
			RANGE_SELECTOR = './tr[2]/td[2]/div/span/text()'
			SPECIFIC_SELECTOR = './tr[2]/td[4]/div/span/text()'
			HABITAT_SELECTOR = './tr[3]/td[2]/div/span/text()'
			FORMULA_SELECTOR = './tr[4]/td[2]/div/span/text()'

			yield {
				'name': hench.xpath(NAME_SELECTOR).extract_first(),
				'level': hench.xpath(LEVEL_SELECTOR).extract_first(),
				'range': hench.xpath(RANGE_SELECTOR).extract_first(),
				'specific': hench.xpath(SPECIFIC_SELECTOR).extract_first(),
				'habitat': hench.xpath(HABITAT_SELECTOR).extract_first(),
				'formula': hench.xpath(FORMULA_SELECTOR).extract_first(),
				'type': response.url.rsplit('/', 1)[-1].rsplit('.', 1)[0]
			}
