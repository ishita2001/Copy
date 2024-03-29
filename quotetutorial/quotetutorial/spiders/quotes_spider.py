
import  scrapy
from ..items import QuotetutorialItem

class Quotespider(scrapy.Spider):

    name = 'quotes'

    start_urls = [
        'http://quotes.toscrape.com/'
    ]

    def parse(self,response):
        item = QuotetutorialItem()
        all_div_quotes = response.css('div.quote')


        for quotes in all_div_quotes:
            title = quotes.css('span.text::text').extract()
            author = quotes.css('.author::text').extract()
            tag = quotes.css('.tag::text').extract()

            item['title'] = title
            item['author'] = author
            item['tag'] = tag

            yield item
