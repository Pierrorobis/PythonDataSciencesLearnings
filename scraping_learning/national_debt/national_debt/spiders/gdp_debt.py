# -*- coding: utf-8 -*-
import scrapy


class GdpDebtSpider(scrapy.Spider):
    name = 'gdp_debt'
    allowed_domains = ['https://worldpopulationreview.com/countries/countries-by-national-debt/']
    start_urls = ['http://https://worldpopulationreview.com/countries/countries-by-national-debt//']

    def parse(self, response):
        pass
