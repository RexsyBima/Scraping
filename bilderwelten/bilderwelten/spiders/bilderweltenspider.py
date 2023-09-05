import scrapy


class BilderweltenspiderSpider(scrapy.Spider):
    name = "bilderweltenspider"
    allowed_domains = ["www.bilderwelten.de"]
    start_urls = ["https://www.bilderwelten.de/p/DRW_1180-custom"]

    def parse_img(self, response):
        img = 

    def parse_name(self, response):
        result = response.css('span.u-d-block ::text').get()
        result = result.replace(' ','')
        return result.replace('\n','')
    
    def parse(self, response):
        yield {
            'title' : self.parse_name(response),
            'url'   : response.url,
            'img_url' : 
        }
