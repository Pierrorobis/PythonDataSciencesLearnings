# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
from urllib.parse import urljoin
import logging


class QuoteSpider(scrapy.Spider):
    name = 'quote'
    allowed_domains = ['quotes.toscrape.com'] # VERY VERY IMPORTANT, OTHERWISE IT WON'T WORK FOR THE NEXT PAGES
    start_urls = ['http://quotes.toscrape.com/js/']

    def start_requests(self):
        for url in self.start_urls:
            yield SplashRequest(url, self.parse_item, args={'wait': 0.5})

    def parse_item(self, response):
        body = response.body
        quotes_selectors = scrapy.Selector(text=body)
        quotes = quotes_selectors.xpath("//div[@class='quote']")

        for quote in quotes:
            yield {
                'quote': quote.xpath("./span[@class='text']/text()").get(),
                'author': quote.xpath("./span/small[@class='author']/text()").get(),
                'tags': quote.xpath("./div[@class='tags']/a[@class='tag']/text()").getall()
            }

        next = response.xpath("//nav/ul/li[@class='next']/a/@href").get()
        if next:
            logging.info(urljoin(response.url, next))
            # Following line does not work
            yield SplashRequest(url=urljoin(response.url, next), callback=self.parse_item, args={'wait': 0.5})
