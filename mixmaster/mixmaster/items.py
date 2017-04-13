# -*- coding: utf-8 -*-

from scrapy import Field, Item

class Core(Item):
	name     = Field()
	level    = Field()
	range    = Field()
	specific = Field()
	type     = Field()

class ImageCore(Item):	
	id         = Field()
	
	image_urls = Field()
	images     = Field()