import scrapy

class Reli_routledgeSpider(scrapy.Spider):
    name = 'Religion'
    allowed_domains = ['tandfonline.com']
    start_urls = ('https://www.tandfonline.com/toc/rrel20/current')

    def parse(self, response):
        sel = Selector
        sites = sel.xpath('//body')
        
        for site in sites:
            site[journal] = sel.xpath('//span[@class="title"]/text()').extract()
            site[publisher] = sel.xpath('//*[@id="e817489e-2520-418b-a731-b62e247e74df"]/div/div/a/text()').extract()
            site[article] = sel.xpath('//div[@class="header"]').extract()
            yield site

