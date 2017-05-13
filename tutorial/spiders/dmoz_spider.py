from scrapy.spiders import Spider
from scrapy.selector import HtmlXPathSelector

class DmozSpider(Spider):
	name = "dmoz"
	allowed_domains = ["dmoztools.net"]
	start_urls = ["http://dmoztools.net/"]
	
	def parse(self, response):
		hxs = HTMLXPathSelector(response)
		sites = hxs.select('//ul/li')

		for site in sites:
			title = site.select('a/text()').extract()
			link = site.select('a/@href').extract()
			desc = site.select('text()').extract()
			print title, link, desc
    




