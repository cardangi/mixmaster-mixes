# -*- coding: utf-8 -*-

import scrapy

class getmix(scrapy.Spider):
	types      = ['dragon', 'beast', 'bird', 'devil', 'insect', 'metal', 'mystic', 'plant']
	url        = 'http://formulasmixmaster.blogspot.com.br/p/{0}.html'
	name       = 'getmixes'
	start_urls = []

	for type in types:
		start_urls = start_urls + [url.format(type)]

	def parse(self, response):
		HENCH_SELECTOR = '//tbody/tr[@style = "height: 18.75pt;"]/..'

		for hench in response.xpath(HENCH_SELECTOR):
			NAME_SELECTOR = './tr/td[2]/div/strong/span/text()'
			LEVEL_SELECTOR = './tr/td[4]/div/span/text()'
			RANGE_SELECTOR = './tr[2]/td[2]/div/span/text()'
			SPECIFIC_SELECTOR = './tr[2]/td[4]/div/span/text()'
			HABITAT_SELECTOR = './tr[3]/td[2]/div/span/text()'
			FORMULA_SELECTOR = './tr[4]/td[2]//text()'

			yield {
				'name': hench.xpath(NAME_SELECTOR).extract_first(),
				'level': hench.xpath(LEVEL_SELECTOR).extract_first(),
				'range': hench.xpath(RANGE_SELECTOR).extract_first(),
				'specific': hench.xpath(SPECIFIC_SELECTOR).extract_first(),
				'habitat': hench.xpath(HABITAT_SELECTOR).extract_first(),
				'formula': fix_formula(", ".join(hench.xpath(FORMULA_SELECTOR).extract())),
				'type': response.url.rsplit('/', 1)[-1].rsplit('.', 1)[0]
			}

def fix_formula(formula):
	return formula.replace('\n, \n, ', '*')  \
				  .replace('\n,', '')         \
				  .replace(', \n', '')         \
				  .replace('*Formula MMHK', '') \
				  .replace(',', '')              \
				  .replace(' *', ', ')            \
				  .replace('\n-  \nFormula MMHK  \n', '')